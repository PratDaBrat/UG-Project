from agent import *
from maze import *
import random
import time
import heapq

X,Y = 70, 70    #random.choice(range(50,100)),random.choice(range(50,100))
W = 0.3         #random.random() * 10000 // 100 / 100 #0.1 #sparseness
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


#helper
def available(m, x, y):
	a = []
	if x + 1 < X and m[y][x+1] not in walls: #R
		a.append(m[y][x+1])
	if y + 1 < Y and m[y+1][x] not in walls: #D
		a.append(m[y+1][x])
	if x - 1 >= 0 and m[y][x-1] not in walls: #L
		a.append(m[y][x-1])
	if y - 1 >= 0 and m[y-1][x] not in walls: #U
		a.append(m[y-1][x])	
	return a

# dijkstra implement (consider A* for quicker?)
'''
1. Determine the starting point of the grid.
2. Record the cost of reaching that agent: 0.
3. Find that agent’s navigable neighbors.
4. For each neighbor, record the cost of reaching the neighbor: +1.
5. For each neighbor, repeat steps 3-5, taking care not to revisit already-visited agents.
'''
## mapping costs
def dijkstra():
	if len(available(plane, s[0].x, s[0].y)) == 0 or len(available(plane, e[0].x, e[0].y)) == 0:
		return 0
	else:
		ref = []
		for _ in plane:
			for __ in _:
				ref.append(__)
		unvisited = [(v.cost,v) for v in ref]
		heapq.heapify(unvisited)

		while len(unvisited):
			uv = heapq.heappop(unvisited)
			cur = uv[1]
			visited.append(cur)
			path.append(cur)
			cur.visited = True
			if cur.group == "end":
				break
			for choice in available(plane, cur.x, cur.y):
				if choice in visited:
					continue
				d = cur.cost + 1
				if d < choice.cost:
					choice.cost = d
					choice.previous = cur
			while len(unvisited):
				heapq.heappop(unvisited)
			unvisited = [(v.cost,v) for v in ref if not v.visited]
			heapq.heapify(unvisited)
			

		end = sorted(e)[0]
		while end.previous:
			final.append(end.previous)
			end = end.previous

		for j in range(Y):
			for i in range(X):
				plane[j][i] = ref[X*j + i]

#random bs
def r():
	cur = s[0]
	while available(plane, cur.x, cur.y):
		if e[0] in available(plane, cur.x, cur.y):
			print("fin")
			break
		cur = random.choice(available(plane, cur.x, cur.y))
		if cur in visited:
			continue
		visited.append(cur)
		final.append(cur)
		cur.visited = True

def __main__():
	start_time = time.time()
	dijkstra()
	t = time.time() - start_time
	#r()
	path_len = len(final)-1
	solve = ""

	if path_len == -1:
		solve = "unsolvable"	
	else:
		#pretty terminal visuals
		m.graphdisp()
		solve = "solved"

	print(f"{X}x{Y} {solve} {t} seconds {W} sparsity {path_len} path")

__main__()
### with random runtime 6.368312835693359 s on 100x100 2d space with 0.2 sparsity of toxin
### with dijkstra program takes way too long to finish executing on a 100x100 2d space
### with dijkstra runtime 10.19450306892395 s on 50x50 2d space with 0.2 sparsity of toxin