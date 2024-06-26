import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from Maze import *
import seaborn as sns
# import pickle
import numpy as np

t,n1,n2 = [],[],[]
ut,un1,un2 = [],[],[]
fig = plt.figure()
ax = plt.axes(projection='3d')
# {X}x{Y} {solve} {t} seconds {W} sparsity {path_len} path
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
