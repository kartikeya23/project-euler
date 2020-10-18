from datetime import datetime
start = datetime.now()

# tr = 3
# tl = 5
# br = 9
# bl = 7

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
while ratio >= 0.1:
	for i in range(4):
		for j in range(i, 4):
			edges[j] += side - 1
	for e in edges:
		if isPrime(e):
			found += 1
	total += 4
	ratio = found / total
	print(f'side: {side}\t\tprimes: {found}\t\tratio: {ratio}')
	side += 2

print(f"\n\nfin in {datetime.now()-start}")