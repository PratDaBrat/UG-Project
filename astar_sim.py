from Maze import *
# import random
import time
from heapq import heappop, heappush
import matplotlib.pyplot as plt


class Node:
	def __init__(self, agent, g_score, h_score):
		self.agent = agent
		self.g_score = g_score
		self.h_score = h_score
		self.f_score = g_score + h_score

	def __lt__(self, other):
		return self.f_score < other.f_score


def manhattan_distance(start, end):
	return abs(start.x - end.x) + abs(start.y - end.y)


def reconstruct_path(came_from, current):
	path = [current]
	while current in came_from:
		current = came_from[current]
		path.append(current)
	return path[::-1]


def available(X, Y, m, x, y, walls):
	a = []
	if x + 1 < X and m[y][x + 1] not in walls: 		# R
		a.append(m[y][x + 1])
	if y + 1 < Y and m[y + 1][x] not in walls: 		# D
		a.append(m[y + 1][x])
	if x - 1 >= 0 and m[y][x - 1] not in walls:		# L
		a.append(m[y][x - 1])
	if y - 1 >= 0 and m[y - 1][x] not in walls:	 	# U
		a.append(m[y - 1][x])
	return a


def a_star(Maze):
	start = Maze.s[0]
	end = Maze.e[0]

	open_set = []
	heappush(open_set, Node(start, 0, manhattan_distance(start, end)))
	closed_set = set()
	came_from = {}
	while open_set:
		current = heappop(open_set)
		if current.agent == end:
			return reconstruct_path(came_from, current.agent)
		closed_set.add(current.agent)
		for neighbor in available(Maze.X, Maze.Y, Maze.plane, current.agent.x, current.agent.y, M.walls):
			tentative_g_score = current.g_score + Maze.updateAgent(neighbor)
			if neighbor not in [node.agent for node in open_set]:
				new_node = Node(neighbor, tentative_g_score, manhattan_distance(neighbor, end))
				heappush(open_set, new_node)
				came_from[neighbor] = current.agent
			elif tentative_g_score < [node.g_score for node in open_set if node.agent == neighbor][0]:
				came_from[neighbor] = current.agent
				for node in open_set:
					if node.agent == neighbor:
						node.g_score = tentative_g_score
						node.f_score = tentative_g_score + node.h_score
						break
	return None


X = []
Y = []
T = []
w = 0.2
for x in range(50, 56):
	for y in range(50, 56):
		M = Maze(x, y, w).generate()
		start_time = time.time()
		path = a_star(M)
		t = time.time() - start_time
		path_len = len(path) - 1
		if path_len != 0:
			X.append(x)
			Y.append(y)
			T.append(t)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(X, Y, T, cmap='viridis', edgecolor='none')
ax.set_xlabel('x of lattice')
ax.set_ylabel('y of lattice')
ax.set_zlabel('time taken in seconds')
plt.show()
