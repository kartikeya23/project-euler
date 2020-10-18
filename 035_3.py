from itertools import permutations, product
from datetime import datetime

start = datetime.now()

odds = [0, 1, 3, 7, 9]

def isPrime(n):
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	if n == 5:
		return True
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

found = set()
for num in product(odds, repeat=6):
	x = int("".join(map(str, num)))
	if isPrime(x):
		found.add(x)
print(f"found {len(found)} such primes")

count = 2
for x in found:
	s = str(x)
	check = True
	for y in permutations(s, len(s)):
		if int("".join(map(str, y))) not in found:
			check = False
			break
	if check:
		count += 1
		print("found \t\t" + s)

print(count)

