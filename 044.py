pents = list()

print("finding all pentagonal numbers")
for n in range(1, 1000):
	p = n * (3 * n - 1) / 2 
	pents.append(p)


l = len(pents)
print("found ", str(l), " numbers")
dmin = 1e9
print("begining search")
for i in range(l):
	for j in range(i+1, l):
		pi = pents[i]
		pj = pents[j]
		d = pj - pi
		if d in pents and sum([pi, pj]) in pents:
			dmin = min([dmin, d])

print(dmin)