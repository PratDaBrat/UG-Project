from cell import *
import random
import time
import heapq

walls = []
s = []
e = []
path = []
X,Y = 150,150 #random.choice(range(50,100)),random.choice(range(50,100))
W = random.random() * 10000 // 100 / 100 #0.1 #sparseness

plane = [[cell(i,j) for i in range(X)] for j in range (Y)]

#maze generation
wall = 0
while wall < W*X*Y:
	x = random.choice(range(0,X))
	y = random.choice(range(0,Y))
	if plane[y][x].group == None:
		plane[y][x] = cell(x,y,"wall") #wall
		walls.append(plane[y][x])
		wall += 1

while True:
	x = random.choice(range(0,X))
	y = random.choice(range(0,Y))
	if plane[y][x].group == None:
		plane[y][x] = cell(x,y,"start",0,True) #start
		s.append(plane[y][x])
		break

while True:
	x = random.choice(range(0,X))
	y = random.choice(range(0,Y))
	if plane[y][x].group == None:
		plane[y][x] = cell(x,y,"end") #end
		e.append(plane[y][x])
		break

visited = [s[0]]
final = []

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
2. Record the cost of reaching that cell: 0.
3. Find that cell’s navigable neighbors.
4. For each neighbor, record the cost of reaching the neighbor: +1.
5. For each neighbor, repeat steps 3-5, taking care not to revisit already-visited cells.
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

		end = e[0]
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
		display = [[" " for i in range(X)] for i in range (Y)]
		for i in range(0,X):
			for j in range(0,Y):
				if plane[j][i] in s:
					display[j][i] = "s"
				elif plane[j][i] in e:
					display[j][i] = "e"
				elif plane[j][i] in walls:
					display[j][i] = "⬝"
				elif plane[j][i] in final:
					display[j][i] = "■"
				
		for n,_ in enumerate(display):
			for __ in _:
				print(__, end=' ')
			print()
		solve = "solved"

	print(f"{X}x{Y} {solve} {t} seconds {W} sparsity {path_len} path")

__main__()
### with random runtime 6.368312835693359 s on 100x100 2d space with 0.2 sparsity of toxin
### with dijkstra program takes way too long to finish executing on a 100x100 2d space
### with dijkstra runtime 10.19450306892395 s on 50x50 2d space with 0.2 sparsity of toxin