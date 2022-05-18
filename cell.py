class cell:
	def __init__(self, x, y, group=None, cost=float('inf'), visited=False):
		self.x = x
		self.y = y
		self.group = group
		self.cost = cost
		self.visited = visited
		self.previous = None

	def __str__(self):
		x = str(self.x)
		y = str(self.y)
		return x + " " + y

	def __lt__(self,other):
		return self.cost < other.cost
