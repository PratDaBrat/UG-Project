#!/usr/bin/env python3
import os, shutil, sys, time
from rl_train import *
import pickle

def main(args):
	PERSISTENCE = False
	SESSIONID = int(time.time())

	if '-p' in args:
		PERSISTENCE = True
	os.mkdir(f'session{SESSIONID}')
	os.mkdir(f'session{SESSIONID}/stateimages')
	os.mkdir(f'session{SESSIONID}/qtables')
	os.mkdir(f'session{SESSIONID}/animations')

	#maze generation
	maze_path = None
	if maze_path is None:
		M = Maze(X,Y,W,FOOD).generate(ENEMY_PENALTY, STAT_PENALTY, FOOD_REWARD)	
	else:
		with open(maze_path,'rb') as f:
			M = pickle.load(f)
	# M.disp()
	c = [X,Y,W,FOOD,EPISODES,MOVE_PENALTY,ENEMY_PENALTY,STAT_PENALTY,FOOD_REWARD,epsilon,EPS_DECAY,LEARNING_RATE,DISCOUNT]
	with open(f'session{SESSIONID}/constants.pickle', 'wb') as f:
			pickle.dump(c,f)

	if '-s' in args:
		with open(f'session{SESSIONID}/maze.pickle', 'wb') as f:
			pickle.dump(M,f)
		
	# for l in reversed(range(1,11)):
	try:
		RL(M,SESSIONID,SHOW_EVERY)
		if not PERSISTENCE:
			shutil.rmtree(f'session{SESSIONID}')
	except:
		if not PERSISTENCE:
			shutil.rmtree(f'session{SESSIONID}')

	return 0

if __name__ == '__main__':
	main(sys.argv)