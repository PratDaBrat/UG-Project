from Maze import *
from tqdm import tqdm
import numpy as np
import time, os
import matplotlib.pyplot as plt
import pickle
from itertools import product

def grid_search_hyperparameters(X, Y):
	"""
	Performs a grid search over learning rate, discount factor, epsilon, and episodes.

	Args:
		X: The width of the maze.
		Y: The height of the maze.

	Returns:
		A dictionary containing the best hyperparameter configuration and its performance.
	"""

	# Define hyperparameter search space
	learning_rates = np.arange(0.1, 0.21, 0.01)
	discount_factors = np.arange(0.7, 0.9, 0.02)
	episodes_list = np.arange(7000, 13000, 1000)

	performance_matrix = np.zeros(shape=[len(learning_rates), len(discount_factors)])
	for episodes in episodes_list:
		M = Maze(X, Y, 0.1, agents=1, food=2).generate(-400, -100, 200)
		S = M.s
		E = M.e
		for i, learning_rate in enumerate(learning_rates):
			for j, discount_factor in enumerate(discount_factors):
				# session = f"hyperparam_tuning_{learning_rate}_{discount_factor}_{epsilon}_{episodes}"
				epsilon = 0.65
				EPS_DECAY = 0.999998
				q_table = np.zeros(shape=[X, Y, 4])
				episode_rewards = []
				# aggr_ep_rewards = {'ep': [], 'avg': [], 'max': [], 'min': []}
				A = S[0]
				# start_time = int(time.time())
				for episode in tqdm(range(episodes + 1), desc='Training RL Model', unit='episode'):
					episode_reward = 0
					steps = 0
					done = False
					while not done and len(E) > 0:
						steps += 1
						qx, qy = A.x, A.y
						if np.random.random() < epsilon:
							act = np.argmax(q_table[qy, qx])
						else:
							act = np.random.choice([0, 1, 2, 3])
						A.action(act)
						reward = M.updateAgent(A)
						episode_reward += reward

						if steps > 180:
							done = True
						elif any((A.x, A.y) == (e.x, e.y) for e in E):
							done = True
						if not done:
							max_future_q = np.max(q_table[A.y, A.x])
							cur_q = q_table[qy, qx, act]
							new_q = (1 - learning_rate) * cur_q + learning_rate * (reward + discount_factor * max_future_q)
							q_table[qy, qx, act] = new_q
						else:
							q_table[qy, qx, act] = 200
					episode_rewards.append(episode_reward)
					epsilon *= EPS_DECAY
					M.reset(M.sinit, M.einit)
				average_reward = sum(episode_rewards) / len(episode_rewards)
				performance_matrix[i, j] = average_reward
		best_config_index = np.unravel_index(performance_matrix.argmax(), performance_matrix.shape)
		best_config = {
			"learning_rate": learning_rates[best_config_index[0]],
			"discount_factor": discount_factors[best_config_index[1]],
		}
		best_performance = performance_matrix.max()
		print(best_config, best_performance)
		print(performance_matrix)
		plt.figure(figsize=(8, 8))
		plt.imshow(performance_matrix, cmap='coolwarm')
		plt.colorbar(label='Average Reward')
		plt.xticks(range(len(learning_rates)), learning_rates, rotation=45)
		plt.yticks(range(len(discount_factors)), discount_factors)
		plt.xlabel('Learning Rate')
		plt.ylabel('Discount Factor')
		plt.title(f'Performance Matrix (Average Reward) for {episodes} Episodes')
		plt.savefig(f'matrix{episodes}.png')
	return best_config


if __name__ == "__main__":
	# Run grid search and print best hyperparameters
	best_config = grid_search_hyperparameters(10, 10)
	# print("Best Hyperparameter Configuration:", best_config)
