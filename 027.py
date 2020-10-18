from datetime import datetime
start = datetime.now()

def isPrime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

def check(n, a, b):
	x = n ** 2 + a * n + b
	if x < 0:
		return False
	if isPrime(x):
		return True
	return False



maxn = 0
prd = 0
for a in range(-1000, 1001):
	for b in range(-1000, 1001):
		n = 0
		while check(n, a, b):
			n += 1
		if n > maxn:
			maxn = n
			prd = a * b
			print(f"n^2\t+\t\t{a}n\t+\t\t{b}\t\t\t0-{maxn}")

print(maxn, prd)

print(f"\n\n\nfin in {datetime.now()-start}")
