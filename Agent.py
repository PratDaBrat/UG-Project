import random

class Agent:
	def __init__(self, x, y, group=None, cost=float('inf'), visited=False, travelPenalty=-1):
		self.x = x
		self.y = y
		self.group = group
		self.cost = cost
		self.visited = visited
		self.travelPenalty = travelPenalty
		self.previous = None
		self.health = 1

	def __str__(self):
		return f"{self.x}, {self.y}"

	def __lt__(self,other):
		return self.cost < other.cost

	def action(self,i):
		if i == 0:
			self.move(1,0)  #R
		elif i == 1:
			self.move(0,1) #D
		elif i == 2:
			self.move(-1,0) #L
		elif i == 3:
			self.move(0,-1)  #U
		else:
			self.move()

	def move(self, x=0, y=0):
		if self.previous is None:
			self.previous = Agent(self.x,self.y)
		if x != 0 or y != 0:
			self.x += x
			self.y += y
		else:
			if random.random() * 10000 // 100 % 2:
				self.x += random.choice([-1,1])
			else:
				self.y += random.choice([-1,1])
