from itertools import permutations
from datetime import datetime

start = datetime.now()

odds = [0, 1, 3, 7] * 6

def isPrime(n):
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

found = [2, 5]
count = 2
for x in permutations(odds, 6):
	num = int("".join(map(str, x)))
	if num > 1 and num not in found:
		if isPrime(num):
			count += 1
			found.append(num)
			print(f"found {count}th\t\t{num}")

def check(f):
	s = str(f)
	global found
	for y in permutations(s, len(s)):
		if int(y) not in found:
			return False
	return True

for f in found:
	if check(f):
		count += 1
print(found)