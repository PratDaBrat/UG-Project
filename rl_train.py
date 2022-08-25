from Maze import *
from animate import makeVideo
from constants import *
import numpy as np
import time, os
import matplotlib.pyplot as plt
import pickle
# from matplotlib import style

# style.use("ggplot")

def RL(M,session,L=LEARNING_RATE):
	start_time = int(time.time())
	LEARNING_RATE = L

	start_q_table = None # or filename using pickle to continue training from certain points

	if start_q_table is None:
		q_table = np.random.uniform(high=0,low=-10,size=[X,Y,4]) #with zeros to discourage repeating moves
		# initialise q_table
		pass
	else:
		with open(start_q_table, 'rb') as f:
			q_table = pickle.load(f)

	S = M.s
	E = M.e
	A = S[0]

	episode_rewards = []
	aggr_ep_rewards = {'ep':[],'avg':[],'max':[],'min':[]}

	for episode in range(EPISODES+1):
		episode_reward = 0
		if not episode % SHOW_EVERY:
			render = True
		else:
			render = False
		i = 0
		completed = 0
		done = False
		while not done and len(E) > 0:
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

			if i > MAX_STEPS:
				done = True
				completed = 0
			elif any((A.x,A.y) == (e.x,e.y) for e in E):
				done = True
				completed += 1
				# r = [e for e in E if (e.x,e.y) == (A.x,A.y)]
				# M.einit.pop(*r)
				# E.remove(*r)
				# M.sinit[A] = (A.x,A.y)
			
			if not done:
				max_future_q = np.max(q_table[A.y,A.x])
				cur_q = q_table[qy,qx,act]
				new_q = (1 - LEARNING_RATE) * cur_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
				q_table[qy,qx,act] = new_q
			else:
				q_table[qy,qx,act] = FOOD_REWARD #1
				break
		
		episode_rewards.append(episode_reward)
		epsilon *= EPS_DECAY
		
		try:
			M.reset()
		except Exception as e:
			print('exception: ',e)

		if render:
			makeVideo(0,i,episode,session,f'session{session}/animations/{episode}.mp4')
			os.system(f'rm -rf session{session}/stateimages/*')
			
		if not episode % STATS_EVERY:
			print(f'on {episode} with epsilon {epsilon}, mean = {np.mean(episode_rewards[-STATS_EVERY:])}')
			average_reward = sum(episode_rewards[-STATS_EVERY:])/STATS_EVERY
			aggr_ep_rewards['ep'].append(episode)
			aggr_ep_rewards['avg'].append(average_reward)
			aggr_ep_rewards['max'].append(max(episode_rewards[-STATS_EVERY:]))
			aggr_ep_rewards['min'].append(min(episode_rewards[-STATS_EVERY:]))
			with open(f'session{session}/qtables/{episode}qtable{X}x{Y}-{int(time.time())-start_time}.pickle', 'wb') as f:
				pickle.dump(q_table, f)

		if completed == 5:
			print(LEARNING_RATE,episode)
			break
	# moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,))/SHOW_EVERY, mode='valid')

	# plt.plot([i for i in range(len(moving_avg))], moving_avg)
	plt.title(f'{X}x{Y} over {EPISODES} episodes')
	plt.ylabel('averages')
	plt.xlabel('episodes')
	plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label="average rewards")
	plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label="max rewards")
	plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label="min rewards")
	plt.legend(loc=2)
	plt.savefig(f'session{session}/stats.png')

	with open(f'session{session}/ep_rewards.pickle', 'wb') as f:
				pickle.dump(episode_rewards, f)
	with open(f'session{session}/aggr_rewards.pickle', 'wb') as f:
				pickle.dump(aggr_ep_rewards, f)