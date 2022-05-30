from Maze import *
from animate_alt import makeVideo
import numpy as np
import time
import matplotlib.pyplot as plt
import pickle
# from matplotlib import style

# style.use("ggplot")

X,Y = 25, 25    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.1         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 1

EPISODES = 10000
MOVE_PENALTY = -1
ENEMY_PENALTY = -10
STAT_PENALTY = -5
FOOD_REWARD = 1

epsilon = 0.9
EPS_DECAY = 0.9998

SHOW_EVERY = 2000

LEARNING_RATE = 0.1
DISCOUNT = 0.95

#maze generation
M = Maze(X,Y,W,FOOD).generate(ENEMY_PENALTY, STAT_PENALTY, FOOD_REWARD)
PLANE = np.array(M.plane)
WALLS = M.walls
S = M.s
E = M.e
FINAL = M.final
PATH = M.path

visited = (S[0])
M.disp()

start_q_table = None # or filename using pickle to continue training from certain points

if start_q_table is None:
	q_table = np.random.uniform(low=-10, high=0, size=[X,Y,4])
	# initialise q_table
	pass
else:
	with open(start_q_table, 'rb') as f:
		q_table = pickle.load(f)

episode_rewards = []
A = S[0]
for episode in range(EPISODES):
	episode_reward = 0
	if not episode % SHOW_EVERY:
		print(f'on {episode} with epsilon {epsilon}, mean = {np.mean(episode_rewards[-SHOW_EVERY:])}')
		render = True
	else:
		render = False
	i = 0
	done = False
	while not done:
		qx, qy = A.x, A.y
		if np.random.random() > epsilon:
			act = np.argmax(q_table[qy,qx])
		else:
			act = np.random.choice([0,1,2,3])
		
		A.action(act)
		reward = M.updateAgent(A) #move complete
		
		if render:
			M.graphDisp(f'stateimages_alt/{episode}_{i}.png')
		i += 1
		episode_reward += reward
		
		if A.x == E[0].x and A.y == E[0].y:
			done = True
		
		if not done:
			max_future_q = np.max(q_table[A.y,A.x])
			cur_q = q_table[qy,qx,act]
			new_q = (1 - LEARNING_RATE) * cur_q + LEARNING_RATE * (reward + DISCOUNT + max_future_q)
			q_table[qy,qx,act] = new_q
		else:
			q_table[qy,qx,act] = 1

	episode_rewards.append(episode_reward)
	epsilon *= EPS_DECAY
	if render:
		makeVideo(0,i,episode,f'animation_alt{episode}.mp4')
	M.reset()

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f'reward {SHOW_EVERY}ma')
plt.xlabel('episode #')
plt.savefig('1maze_rlstats.png')

with open(f'qtables/1maze_qtable-{int(time.time())}.pickle', 'wb') as f:
	pickle.dump(q_table, f)
