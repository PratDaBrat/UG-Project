from maze import *
import numpy as np
import time, random

X,Y = 15, 15    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.1         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
food = 1

#maze generation
m = maze(X,Y,W,food).generate()
plane = np.array(m.plane)
walls = m.walls
s = m.s
e = m.e
final = m.final
path = m.path
copy = np.copy(plane)

visited = [s[0]]
m.disp()