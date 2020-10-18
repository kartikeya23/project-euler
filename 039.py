from datetime import datetime
start = datetime.now()

from math import sqrt

top = int(1e3) + 1
highest = 0
at = 0
for p in range(2, top, 2):
	count = 0
	print("p={}".format(p))
	for a in range(1, p // 2):
		for b in range(a + 1, min(sqrt(p**2 - a**2), p - a - 1)):
			c = p - (a + b)
			if c**2 == a**2 + b**2 and c == int(c):
				count += 1
				# print(f"{a}\t\t{b}\t\t{c}")
	if count > highest:
		highest = count
		at = p
	# print("\n\n")

print(at, highest)

print(f"\n\n\nfin in {datetime.now()-start}")
