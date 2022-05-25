from agent import *
from maze import *

X,Y,W,food = 4,4,0.1,1

m = maze(X,Y,W,food).generate()
# m.disp()
a = m.s[0]

for i in [0,1,2,3]:
	a.action(i)
	m.updateAgent(a)
