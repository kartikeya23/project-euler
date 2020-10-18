from functools import reduce

def isPrime(n):
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

def npf(n):
	fact = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	ret = set()
	for f in fact:
		if isPrime(f):
			ret.add(f)
	return len(ret) - 1

i = 2 * 3 * 5 * 7

while True:
	print(f"checking {i}")
	if npf(i) == 4:
		if npf(i+1) == 4:
			if npf(i+2) == 4:
				if npf(i+3) == 4:
					print(i, i+1, i+2, i+3)
					break
	i += 1