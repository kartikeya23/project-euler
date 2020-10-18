from datetime import datetime
start = datetime.now()

from helper import factors, isPrime

tot = 0
for n in range(1, 100000001):
	flag = True
	for y in factors(n):
		if not isPrime(y + n / y):
			flag = False
			break
	if flag:
		print(n)
		tot += n
		


print(f"\n\n\nfin in {datetime.now()-start}")
