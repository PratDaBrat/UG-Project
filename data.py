import matplotlib.pyplot as plt

file = open('times75x75.txt','r')
solved = []
unsolved = []

N = 1050
m = [0 for _ in range(N)]

for i in range(N):
	arr = file.readline().split()
	m[i] = arr

s, t = [], []
us, ut = [], []
# ax = [i for i in range(N)]

for entry in m:
	if entry[1] == 'solved':
		s += [float(entry[4])]
		t += [float(entry[2]) if 'e' not in entry[2] else 0]
	if entry[1] == 'unsolvable':
		us += [float(entry[4])]
		ut += [float(entry[2]) if 'e' not in entry[2] else 0]

plt.scatter(us,ut,c='red',s=10)
plt.scatter(s,t,s=15)
plt.show()