from datetime import datetime
start = datetime.now()

from itertools import permutations

nums = [str(i) for i in range(1, 10)]
pans = [x for x in map(lambda a: "".join(a), permutations(nums))]


def myf(x):
	s = str(x)
	m = 2
	while len(s) < 9:
		s += str(x * m)
		m += 1
	return s


x = 1
while x < 1e5:
	s = myf(x)
	if s in pans:
		print(F"found: {s}")
	x += 1



print(f"finished in {datetime.now() - start}")
