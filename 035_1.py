from itertools import permutations

print("finding primes")
def isPrime(n):
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True


p = [2]
x = 3
while x < 1e6:
	if isPrime(x):
		p.append(str(x))
	x += 2

print(f"found {len(p)} primes")

count = 0
for x in p:
	check = True
	s = str(x)
	for y in permutations(s, len(s)):
		c = "".join(y)
		# print(c)
		if c not in p:
			check = False
	if check:
		count += 1
		print(f"found {count}th circ prime \t\t{x}")
