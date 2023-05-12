import matplotlib.pyplot as plt
# import seaborn as sns

file = open('times100x100.txt','r')
solved = []
unsolved = []

N = 1800
m = [0 for _ in range(N)]

for i in range(N):
	arr = file.readline().split()
	m[i] = arr

s, t = [], []
us, ut = [], []
# ax = [i for i in range(N)]

#{X}x{Y} {solve} {t} seconds {W} sparsity {path_len} path
#   0       1     2     3     4     5         6       7

for entry in m:
	if entry[1] == 'solved' and int(entry[6]) > 5:
		s += [float(entry[4])]
		t += [float(entry[2]) if 'e' not in entry[2] else 0]
	if entry[1] == 'unsolvable' and float(entry[2]) > 0.0003:
		us += [float(entry[4])]
		ut += [float(entry[2]) if 'e' not in entry[2] else 0]

plt.title(f"Relation between W and t for {entry[0]} sized lattice")
plt.xlabel("Sparsities (W)")
plt.ylabel("Times (t)")
plt.scatter(us,ut,c='red',s=10)
plt.scatter(s,t,s=15)
plt.legend(["unsolved","solved"],loc=1)
plt.show()