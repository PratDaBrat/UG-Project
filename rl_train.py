from Maze import *
from animate import makeVideo, makeQTV
from graph import *
from tqdm import tqdm
import numpy as np
import time, os
import matplotlib.pyplot as plt
import pickle
from constants import *


def RL(M, session):
	S = M.s
	E = M.e
	# LEARNING_RATE = 0.2
	epsilon = 0.65
	start_q_table = None		# or filename using pickle to continue training from certain points

	if start_q_table is None:
		q_table = np.zeros(shape=[M.X, M.Y, 4])		# initialise q_table
		# q_table = np.random.uniform(high=2, low=1, size=[X, Y, 4]) 	# with zeros to discourage repeating moves
	else:
		with open(start_q_table, 'rb') as f:
			q_table = pickle.load(f)

	episode_rewards = []
	aggr_ep_rewards = {'ep': [], 'avg': [], 'max': [], 'min': []}
	A = S[0]
	# completed = 0
	start_time = int(time.time())
	for episode in tqdm(range(EPISODES + 1), desc='Training RL Model', unit='episode'):
		episode_reward = 0
		if not episode % SHOW_EVERY:
			render = True
		else:
			render = False

		i = 0
		done = False
		while not done and len(E) > 0:
			i += 1
			qx, qy = A.x, A.y
			if np.random.random() > epsilon:
				act = np.argmax(q_table[qy, qx])
			else:
				act = np.random.choice([0, 1, 2, 3])
			A.action(act)
			reward = M.updateAgent(A)		#move complete	
			episode_reward += reward

			if i > MAX_STEPS:
				done = True
			elif any((A.x, A.y) == (e.x, e.y) for e in E):
				done = True
			if not done:
				max_future_q = np.max(q_table[A.y, A.x])
				cur_q = q_table[qy, qx, act]
				new_q = (1 - LEARNING_RATE) * cur_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
				q_table[qy, qx, act] = new_q
			else:
				q_table[qy, qx, act] = FOOD_REWARD

			if render:
				QTDisp(M, q_table, f'session{session}/qtimages/{episode}_{i}.png')

			if done:
				break

		episode_rewards.append(episode_reward)
		epsilon *= EPS_DECAY
		M.reset(M.sinit, M.einit)

		if render:
			makeQTV(1, i, episode, session, f'session{session}/animations/qt_{episode}.mp4')
			os.system(f'rm -rf session{session}/qtimages/*')

		if not episode % STATS_EVERY:
			# print(f'on {episode} with epsilon {epsilon}, mean = {np.mean(episode_rewards[-STATS_EVERY:])}')
			average_reward = sum(episode_rewards[-STATS_EVERY:]) / STATS_EVERY
			aggr_ep_rewards['ep'].append(episode)
			aggr_ep_rewards['avg'].append(average_reward)
			aggr_ep_rewards['max'].append(max(episode_rewards[-STATS_EVERY:]))
			aggr_ep_rewards['min'].append(min(episode_rewards[-STATS_EVERY:]))
			with open(f'session{session}/qtables/{episode}qtable{X}x{Y}-{int(time.time())-start_time}.pickle', 'wb') as f:
				pickle.dump(q_table, f)

	# moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')
	# plt.plot([i for i in range(len(moving_avg))], moving_avg)
	plt.title(f'{X}x{Y} over {EPISODES} episodes')  # completed {completed} times')
	plt.ylabel('averages')
	plt.xlabel('episodes')
	plt.xticks(np.arange(0, EPISODES+1, 500))
	# plt.yticks(np.arange(min(),max(re)))
	plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label="average rewards")
	plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label="max rewards")
	plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label="min rewards")
	plt.legend(loc=4)
	plt.savefig(f'session{session}/stats.png')

	with open(f'session{session}/ep_rewards.pickle', 'wb') as f:
		pickle.dump(episode_rewards, f)
	with open(f'session{session}/aggr_rewards.pickle', 'wb') as f:
		pickle.dump(aggr_ep_rewards, f)
