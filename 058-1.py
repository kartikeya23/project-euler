from datetime import datetime
start = datetime.now()

edges = [3, 5, 9, 7]
side = 5
found = 3
total = 5

def isPrime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

ratio = found / total
x = 9
while ratio >= 0.1:
	# check for primes at edges
	offset = side - 1
	j = 0
	for i in range(1, 5):
		j += offset
		if isPrime(x+j):
			# print(f"{x+j} is prime")
			found += 1
	x = side * side
	total += 4
	ratio = found / total
	print(f'side: {side}\t\tprimes: {found}\t\tratio: {ratio}')
	side += 2

print(f"\n\nfin in {datetime.now()-start}")