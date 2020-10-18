from itertools import permutations

def isPrime(n):
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True


x = 3
count = 1
while x < 1e6:
	if isPrime(x):
		s = str(x)
		check = True
		for y in permutations(s, len(s)):
			if not isPrime(int("".join(s))):
				check = False
				break
		if check:
			count += 1
			print(f"found {count}th circular prime\t{s}")
	x += 2
	