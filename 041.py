from datetime import datetime
start = datetime.now()

def isPrime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True


from itertools import permutations

for n in range(2, 10):
	x = [str(i) for i in range(1, n+1)]
	for num in list(map(lambda a: int("".join(a)), permutations(x))):
		if isPrime(num):
			print(num)


print(f"\n\n\nfin in {datetime.now()-start}")
