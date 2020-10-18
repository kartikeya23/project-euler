from datetime import datetime
start = datetime.now()

from math import sqrt

def phi(n):
	res = n
	p = 2
	while p <= sqrt(n):
		if n % p == 0:
			while n % p == 0:
				n //= p
			res *= (1 - 1 / p)
		p += 1
	if n > 1:
		res *= (1 - 1 / n)
	return int(res)

max_r = 2
at = 2
for n in range(3, 1000001):
	r = n / phi(n)
	if r > max_r:
		max_r = r
		at = n
		print(f"{n}\t\t\t{r}")

print(F"\n\nans:{n}\t\t{r}")

print(f"\n\n\nfin in {datetime.now()-start}")
