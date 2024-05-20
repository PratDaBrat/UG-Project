import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import Polygon
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import get_cmap
from Maze import *
# import pickle
import numpy as np

def visMaze(ax, maze):
	color_map = {
		0: np.array([50, 20, 0]),			# plain
		1: np.array([255, 0, 0]),			# agent
		2: np.array([31, 247, 2]),			# food
		3: np.array([2, 94, 171]),			# walls
		4: np.array([150, 150, 150])		# path
		}

	maze.display = [[color_map[0] for i in range(maze.X)] for i in range(maze.Y)]

	for i in range(0, maze.X):
		for j in range(0, maze.Y):
			if maze.plane[j][i] in maze.s:
				maze.display[j][i] = color_map[1]
			elif maze.plane[j][i] in maze.e:
				maze.display[j][i] = color_map[2]
			elif maze.plane[j][i] in maze.walls:
				maze.display[j][i] = color_map[3]
			elif maze.plane[j][i] in maze.final:
				maze.display[j][i] = color_map[4]

	ax.set_title("Maze")
	canvas = np.array(maze.display)
	ax.set_xticks([])
	ax.set_yticks([])
	img = plt.imshow(canvas, interpolation=None)
	# print('visMaze complete')
	return img


def visQTable(ax, q_table):

	x, y, num_actions = q_table.shape

	# cmap = LinearSegmentedColormap.from_list('grayscale', [(0, 'black'), (1, 'white')])
	# color_map = lambda q_value 
	cmap = get_cmap('RdYlBu')

	for i in range(x):
		for j in range(y):
			q_values = q_table[j][i]
			q_min, q_max = np.min(q_values), np.max(q_values)
			for _ in range(num_actions):
				q_value = q_table[j][i][_]
				# print(q_value)
				vertices = [[(i, j), (i + 0.5, j - 0.5), (i + 0.5, j + 0.5)],
							[(i, j), (i + 0.5, j - 0.5), (i - 0.5, j - 0.5)],
							[(i, j), (i - 0.5, j + 0.5), (i - 0.5, j - 0.5)],
							[(i, j), (i - 0.5, j + 0.5), (i + 0.5, j + 0.5)]]
				q_color = (q_value - q_min) / (q_max - q_min)
				ax.add_patch(Polygon(vertices[_], closed=True, color=cmap(q_color)))

	ax.set_title("Q-Table Heatmap")
	ax.set_xticks(np.arange(-0.5, x + 0.5))
	ax.set_yticks(np.arange(-0.5, y + 0.5))
	ax.invert_yaxis()
	ax.xaxis.set_major_locator(ticker.NullLocator())
	ax.yaxis.set_major_locator(ticker.NullLocator())
	# print('visQTable complete')


def QTDisp(maze, q_table, name):
	fig, axs = plt.subplots(1, 2, figsize=(12, 6))
	visQTable(axs[0], q_table)
	visMaze(axs[1], maze)
	plt.savefig(name)
	plt.close()
	# print('QTDisp complete')


''' usage

SESSIONID = "1714509663"
l = []

with open('qtables.txt', 'rb') as f:
	for _ in f:
		l.append(str(_.strip())[2:-1])

f.close()
with open (f'session{SESSIONID}/maze.pickle', 'rb') as f:
	M = pickle.load(f)
f.close()

for filename in l:
	with open(f'session{SESSIONID}/qtables/{filename}', 'rb') as f:
		q_table = pickle.load(f)
		q_min, q_max = np.min(q_table), np.max(q_table)
		q_table = (q_table - q_min) / (q_max - q_min)
		QTDisp(M, q_table, f'session{SESSIONID}/qtimages/{filename}.png')

f.close()
'''
