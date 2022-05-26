from Maze import *
import random

X,Y,W,food = 10,10,0.1,1

m = Maze(X,Y,W,food).generate()
a = m.s[0]
travel = 0
done = False
i = 0
while i <= 20:
	# m.disp()
	print(m.getActionSpace())
	m.graphDisp(f'stateimages/{i}.png')
	a.action(random.choice(m.getActionSpace()))
	travel += m.updateAgent(a)
	i += 1
print(travel)