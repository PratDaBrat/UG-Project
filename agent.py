class agent:
	def __init__(self, x, y, group=None, cost=float('inf'), visited=False):
		self.x = x
		self.y = y
		self.group = group
		self.cost = cost
		self.visited = visited
		self.previous = None
		self.health = 1

	def __str__(self):
		return f"{self.x}, {self.y}"

	def __lt__(self,other):
		return self.cost < other.cost
