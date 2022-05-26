from Maze import *

X,Y,W,food = 10,10,0.5,1

m = Maze(X,Y,W,food).generate()
a = m.s[0]
travel = 0
for i in [0,1,2,3]:
	# m.graphDisp(f'stateimages/{i}.png')
	a.action(i)
	travel += m.updateAgent(a)
print(travel)