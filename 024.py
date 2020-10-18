import itertools

x = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

n = 0
for c in x[int(1e6 - 1)]:
	n = n * 10 + c

print(n)