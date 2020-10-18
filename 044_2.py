from datetime import datetime
start = datetime.now()

from math import sqrt

def isPent(n):
	x = (sqrt(24 * n + 1) + 1) / 6
	return x.is_integer()


# p = n * (3 * n - 1) / 2 
i = 2
while True:
	pi = i * (3 * i - 1) / 2 
	for j in range(1, i - 1):
		pj = j * (3 * j - 1) / 2
		if isPent(pi - pj) and isPent(pi + pj):
			print(f"{pi}\t\t\t{pj}\t\t\t{pi-pj}")
	i += 1
	
print(f"\n\n\nfin in {datetime.now()-start}")
