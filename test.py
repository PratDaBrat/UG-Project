from Maze import *
import random

X,Y,W,FOOD = 5,5,0.1,1

M = Maze(X,Y,W,FOOD).generate()
PLANE = np.array(M.plane)
WALLS = M.walls
S = M.s
E = M.e
FINAL = M.final
PATH = M.path
A = M.s[0]
travel = []
done = False
i = 0
while i <= 20:
	# m.disp()
	# print(m.getActionSpace())
	M.graphDisp(f'stateimages/{i}.png')
	A.action(random.choice([0,1,2,3]))
	travel.append(M.updateAgent(A))
	i += 1
	M.reset()
print(travel)
print(sum(travel))
