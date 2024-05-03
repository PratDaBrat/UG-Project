import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import Polygon
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.cm import get_cmap
from Maze import *
# import seaborn as sns
# import pickle
import numpy as np

# t,n1,n2 = [],[],[]
# ut,un1,un2 = [],[],[]
# fig = plt.figure()
# ax = plt.axes(projection='3d')
#{X}x{Y} {solve} {t} seconds {W} sparsity {path_len} path
#   0       1     2     3     4     5         6       7
'''
file = open("data/Dijkstra/70x70_30.txt",'r')
for i in range(3600):
	arr = file.readline().split()
	if arr[1] == 'solved':
		n1.append(int(arr[0][:2]))
		t.append(float(arr[2]))
		n2.append(int(arr[0][-2:]))
	else :
		un1.append(int(arr[0][:2]))
		ut.append(float(arr[2]))
		un2.append(int(arr[0][-2:]))

st = sorted(list(zip(s,t)))
s = [s[0] for s in st]
t = [t[1] for t in st]
# ax.scatter3D(n1,n2,t)

ust = sorted(list(zip(us,ut)))
us = [s[0] for s in ust]
ut = [t[1] for t in ust]
# ax.scatter3D(un1,un2,ut,color='red')
'''
''' probability distribution
t = np.array(sorted(t))
mean = statistics.mean(t)
sd = statistics.stdev(t)
'''
# plt.plot(t,norm.pdf(t,mean,sd))
# ax.set_zlabel("t in seconds")
# ax.set_xlabel("x of lattice")
# ax.set_ylabel("y of lattice")
# ax.set_title("random lattices at fixed sparsity")
# plt.show()


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
	cmap = get_cmap('coolwarm')

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
