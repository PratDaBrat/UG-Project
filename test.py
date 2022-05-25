from Maze import *

X,Y,W,food = 4,4,0.1,1

m = Maze(X,Y,W,food).generate()
m.disp()
a = m.s[0]
a.action(1)
print(a.previous)
print(a)
# for i in [0,1,2,3]:
# 	a.action(i)
# 	m.updateAgent(a)
