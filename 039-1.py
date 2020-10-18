from datetime import datetime
start = datetime.now()

from math import sqrt

top = 1e3
highest = 0
at = 0

p = 2
while p <= top:
	count = 0
	a = 2
	while a < (p / 3):
		if (p*(p-2*a)) % (2*(p-a)) == 0:
			count +=1
		a += 1
	print(f"p={p}\t\t{count}")
	if count > highest:
		highest = count
		at = p
	p += 2


print(at, highest)

print(f"\n\n\nfin in {datetime.now()-start}")
