from cell import *
import random

class maze():
	def __init__(self, X, Y, sparsity, m=1):
		self.X = X
		self.Y = Y
		self.sparsity = sparsity
		self.max = m
		self.walls = []
		self.s = []
		self.e = []
		self.final = []
		self.path = []
		self.plane = [[cell(i,j) for i in range(X)] for j in range (Y)]
		self.display = [[" " for i in range(X)] for i in range (Y)]

	def generate(self):
		wall = 0
		while wall < self.sparsity * self.X * self.Y:
			x = random.choice(range(0,self.X))
			y = random.choice(range(0,self.Y))
			if self.plane[y][x].group == None:
				self.plane[y][x] = cell(x,y,"wall") #wall
				self.walls.append(self.plane[y][x])
				wall += 1

		while len(self.e) <= 1:
			x = random.choice(range(0,self.X))
			y = random.choice(range(0,self.Y))
			if self.plane[y][x].group == None:
				self.plane[y][x] = cell(x,y,"start",0,True) #start
				self.s.append(self.plane[y][x])
				break

		while len(self.e) < self.max:
			x = random.choice(range(0,self.X))
			y = random.choice(range(0,self.Y))
			if self.plane[y][x].group == None:
				self.plane[y][x] = cell(x,y,"end") #end
				self.e.append(self.plane[y][x])
		return self

	def disp(self):
		plane = self.generate().plane
		for i in range(0,self.X):
			for j in range(0,self.Y):
				if plane[j][i] in self.s:
					self.display[j][i] = "s"
				elif plane[j][i] in self.e:
					self.display[j][i] = "e"
				elif plane[j][i] in self.walls:
					self.display[j][i] = "⬝"
				elif plane[j][i] in self.final:
					self.display[j][i] = "■"
				
		for n,_ in enumerate(self.display):
			for __ in _:
				print(__, end=' ')
			print()

# m = maze(50,50,0.1,3).generate()
# m.disp()
