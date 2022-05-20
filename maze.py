from agent import *
import random
import matplotlib.pyplot as plt
import numpy as np

class maze():
	def __init__(self, X, Y, sparsity, food=1):
		self.X = X
		self.Y = Y
		self.sparsity = sparsity
		self.food = food
		self.walls = []
		self.s = []
		self.e = []
		self.final = []
		self.path = []
		self.plane = [[agent(i,j) for i in range(X)] for j in range (Y)]
		self.display = [[' ' for i in range(X)] for i in range (Y)]

	def generate(self):
		while len(self.walls) < self.sparsity * self.X * self.Y:
			x = random.choice(range(0,self.X))
			y = random.choice(range(0,self.Y))
			if self.plane[y][x].group == None:
				self.plane[y][x] = agent(x,y,"wall") #wall
				self.walls.append(self.plane[y][x])

		while len(self.e) < 1:
			x = random.choice(range(0,self.X))
			y = random.choice(range(0,self.Y))
			if self.plane[y][x].group == None:
				self.plane[y][x] = agent(x,y,"start",0,True) #start
				self.s.append(self.plane[y][x])
				break

		while len(self.e) < self.food:
			x = random.choice(range(0,self.X))
			y = random.choice(range(0,self.Y))
			if self.plane[y][x].group == None:
				self.plane[y][x] = agent(x,y,"end") #end
				self.e.append(self.plane[y][x])

		for i in range(0,self.X):
			for j in range(0,self.Y):
				if self.plane[j][i] in self.s:
					self.display[j][i] = "s"
				elif self.plane[j][i] in self.e:
					self.display[j][i] = "e"
				elif self.plane[j][i] in self.walls:
					self.display[j][i] = "⬝"
				elif self.plane[j][i] in self.final:
					self.display[j][i] = "■"
		return self

	def disp(self):				
		for n,_ in enumerate(self.display):
			for __ in _:
				print(__, end=' ')
			print()

	def graphdisp(self):
		color_map = {0: np.array([50, 20, 0]),# plain
		1: np.array([255, 0, 0]),# agent
		2: np.array([31, 247, 2]),# food
		3: np.array([2, 94, 171]),# walls
		4: np.array([150, 150, 150])} # path
		
		self.display = [[color_map[0] for i in range(self.X)] for i in range (self.Y)]
		
		for i in range(0,self.X):
			for j in range(0,self.Y):
				if self.plane[j][i] in self.s:
					self.display[j][i] = color_map[1]
				elif self.plane[j][i] in self.e:
					self.display[j][i] = color_map[2]
				elif self.plane[j][i] in self.walls:
					self.display[j][i] = color_map[3] 
				elif self.plane[j][i] in self.final:
					self.display[j][i] = color_map[4]

		plt.grid(False)
		ax = plt.gca()
		ax.set_xticks([])
		ax.set_yticks([])
		canvas = np.array(self.display)
		'''
		for i in range(0, canvas.shape[0]):
			for j in range(0, canvas.shape[1]):
				c = canvas[j,i]
				ax.text(i, j, str(c), va='center', ha='center')
		'''
		img = plt.imshow(canvas, interpolation='none')
		plt.savefig('test.png')
		return img

m = maze(100,50,0.05,30).generate()
# m.disp()
m.graphdisp()
