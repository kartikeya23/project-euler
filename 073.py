from datetime import datetime
start = datetime.now()

from fractions import Fraction
from math import gcd

l = set()
count = 0
for d in range(1, 12001):
	for n in range(d//3 + 1, int(d / 2 + 0.5)):
		g = gcd(n, d)
		l.add((n/g, d/g))
		print(f"{n}\t\t\t/\t\t\t{d}")

print(f"found {len(l)} such numbers")


print(f"finished in {datetime.now() - start}")
