from Maze import *
import random
from animate import makeVideo

X,Y,W,FOOD = 30,30,0.1,1

M = Maze(X,Y,W,FOOD).generate()
PLANE = np.array(M.plane)
WALLS = M.walls
S = M.s
E = M.e
FINAL = M.final
PATH = M.path
A = M.s[0]
RESET = 10
travel = []
done = False
i = 0
while i <= 50:
	# m.disp()
	# print(m.getActionSpace())
	M.graphDisp(f'stateimages/{i}.png')
	if A.x <= 15 and A.y <= 15:
		A.action(random.choice([0,1]))
	elif A.x > 15 and A.y > 15:
		A.action(random.choice([2,3]))
	elif A.x <= 15 and A.y > 15:
		A.action(random.choice([3,1]))
	if A.x > 15 and A.y <= 15:
		A.action(random.choice([0,2]))
	travel.append(M.updateAgent(A))
	i += 1
	if i % RESET == 0:
		M.reset()
		makeVideo((i//RESET - 1)*RESET,i,f'animation{i}.mp4')
print(travel)
print(sum(travel))
