def isPrime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

total = 2
for x in range(3, 2000000):
	if isPrime(x):
		total += x

print(total)

