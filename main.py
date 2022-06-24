#!/usr/bin/env python3
import os, shutil, sys, time
from rl_sim import *

def main(args):
	PERSISTENCE = False
	SESSIONID = int(time.time())

	if '-p' in args:
		PERSISTENCE = True
	os.mkdir(f'session{SESSIONID}')
	os.mkdir(f'session{SESSIONID}/stateimages')
	os.mkdir(f'session{SESSIONID}/qtables')

	#maze generation
	M = Maze(X,Y,W,FOOD).generate(ENEMY_PENALTY, STAT_PENALTY, FOOD_REWARD)
	# M.disp()
	RL(M,SESSIONID)

	if not PERSISTENCE:
		shutil.rmtree(f'session{SESSIONID}')
	return 0

if __name__ == '__main__':
	main(sys.argv)