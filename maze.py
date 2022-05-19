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
		return self

	def disp(self):
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
				
		for n,_ in enumerate(self.display):
			for __ in _:
				print(__, end=' ')
			print()

	def graphdisp(self):
		self.display = [[0.9 for i in range(self.X)] for i in range (self.Y)]
		for i in range(0,self.X):
			for j in range(0,self.Y):
				if self.plane[j][i] in self.s:
					self.display[j][i] = 0.5
				elif self.plane[j][i] in self.e:
					self.display[j][i] = 0.7
				elif self.plane[j][i] in self.walls:
					self.display[j][i] = 0.2 
				elif self.plane[j][i] in self.final:
					self.display[j][i] = 0.0

		plt.grid('on')
		ax = plt.gca()
		ax.set_xticks(np.arange(0.5, self.Y, 1))
		ax.set_yticks(np.arange(0.5, self.X, 1))
		canvas = np.array(self.display)
		print(canvas)
		img = plt.imshow(canvas, interpolation='none')
		plt.savefig('test.png')
		return img

m = maze(10,10,0.1,1).generate()
# m.disp()
m.graphdisp()
