from datetime import datetime
start = datetime.now()

from helper import getDgts
from itertools import permutations

def isCube(n):
	return round(n ** (1./3.)) ** 3 == n


def checker(n):
	perms = set(int("".join(x)) for x in permutations(str(n)))
	perms = [p for p in perms if len(str(p)) == len(str(n))]
	c = 0
	for p in perms:
		if isCube(p):
			c += 1
	return c


x = 1
y = checker(x**3)
while y != 5:
	print(f"{x}\t\t\t{y}")
	x += 1
	y = checker(x**3)

print(f"\n\n\n{x}\t\t\t{(x-1)}")


print(f"finished in {datetime.now() - start}")
