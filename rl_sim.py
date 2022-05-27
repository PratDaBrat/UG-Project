from Maze import *
import numpy as np
import time, random
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style

style.use("ggplot")

X,Y = 15, 15    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.1         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
FOOD = 1

EPISODES = 25000
MOVE_PENALTY = -1
ENEMY_PENALTY = -100
FOOD_REWARD = 1

epsilon = 0.9
EPS_DECAY = 0.9998

SHOW_EVERY = 5000

LEARNING_RATE = 0.1
DISCOUNT = 0.95

#maze generation
M = Maze(X,Y,W,FOOD).generate()
PLANE = np.array(m.plane)
WALLS = m.walls
S = m.s
E = m.e
FINAL = m.final
PATH = m.path

visited = (s[0])
m.disp()

start_q_table = None # or filename using pickle to continue training from certain points

if start_q_table is None:
	q_table = {}
	for y in range(-Y+1, Y):
		for x in range(-X+1, X):