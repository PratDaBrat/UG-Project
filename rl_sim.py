from maze import *
import time
import random

X,Y = 20, 20    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.1         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
food = 1

#maze generation
m = maze(X,Y,W,food).generate()
plane = m.plane
walls = m.walls
s = m.s
e = m.e
final = m.final
path = m.path

visited = [s[0]]

