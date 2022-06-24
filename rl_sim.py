from Maze import *
from animate import makeVideo
from constants import *
import numpy as np
import time
# import matplotlib.pyplot as plt
import pickle
# from matplotlib import style

# style.use("ggplot")

def RL(M,session):
	S = M.s
	E = M.e
	epsilon = 0.85
	start_q_table = None # or filename using pickle to continue training from certain points

	if start_q_table is None:
		q_table = np.random.uniform(high=0,low=-10,size=[X,Y,4]) #with zeros to discourage repeating moves
		# initialise q_table
		pass
	else:
		with open(start_q_table, 'rb') as f:
			q_table = pickle.load(f)

	episode_rewards = []
	A = S[0]
	for episode in range(EPISODES+1):
		episode_reward = 0
		if not episode % SHOW_EVERY:
			print(f'on {episode} with epsilon {epsilon}, mean = {np.mean(episode_rewards[-SHOW_EVERY:])}')
			render = True
		else:
			render = False
		i = 0
		done = False
		steps = 0 #temp
		while not done:
			qx, qy = A.x, A.y
			if np.random.random() > epsilon:
				act = np.argmax(q_table[qy,qx])
			else:
				act = np.random.choice([0,1,2,3])
			
			A.action(act)
			reward = M.updateAgent(A) #move complete
			
			if render:
				M.graphDisp(f'session{session}/stateimages/{episode}_{i}.png')
			i += 1
			episode_reward += reward

			if steps > 200:  #temp
				done = True
			elif any((A.x,A.y) == (e.x,e.y) for e in E):
				done = True
			if not done:
				max_future_q = np.max(q_table[A.y,A.x])
				cur_q = q_table[qy,qx,act]
				new_q = (1 - LEARNING_RATE) * cur_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
				q_table[qy,qx,act] = new_q
				steps += 1
			else:
				q_table[qy,qx,act] = 1

		episode_rewards.append(episode_reward)
		epsilon *= EPS_DECAY
		if render:
			makeVideo(0,i,episode,session,f'{session}animation{episode}.mp4')
		M.reset()

	# moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')

	# plt.plot([i for i in range(len(moving_avg))], moving_avg)
	# plt.ylabel(f'reward {SHOW_EVERY}ma')
	# plt.xlabel('episode #')
	# plt.savefig('data/{session}rlstats.png')

	with open(f'session{session}/qtables/qtable{X}x{Y}-{int(time.time())}.pickle', 'wb') as f:
		pickle.dump(q_table, f)