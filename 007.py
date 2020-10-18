def isPrime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

count = 3
x = 3
while count < 1e4+2:
	x += 2
	if isPrime(x):
		count += 1
print(x)