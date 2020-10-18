from math import sqrt

top = int(1e5)

def checkPent(n):
	x = (sqrt(24 * n + 1) + 1) / 6
	return x.is_integer()

d = 1e10
for i in range(1 , top):
	for j in range(i+1, top):
		pi = i * (3 * i - 1) / 2
		pj = j * (3 * j - 1) / 2
		dji = pj - pi
		add = pj + pi
		if checkPent(add) and checkPent(dji):
			print(f"found pair {pj}\t\t{pi}")
			d = min([d, dji])
		else:
			print(f"{i}\t{j} rejected")