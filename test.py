from Maze import *

X,Y,W,food = 10,10,0,1

m = Maze(X,Y,W,food).generate()
a = m.s[0]
for i in [0,1,2,3]:
	m.graphDisp(f'stateimages/{i}.png')
	a.action(i)
	m.updateAgent(a)
