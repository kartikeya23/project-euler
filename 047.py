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

def p_factors(n):
	fact = set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	ret = set()
	for f in fact:
		if isPrime(f):
			ret.add(f)
	return ret

f = [set([])]

def len_check(x):
	global f
	for i in range(x-3, x+1):
		if len(f[i]) != 4:
			return False

for x in range(1, 5):
	f.append(p_factors(x))

print(f)

found = False
x = 5
while not found:
	f.append(p_factors(x))
	y = f[x].intersection(f[x-1]).intersection(f[x-2]).intersection(f[x-3]).remove(1)
	print(y)
	if y == None and len_check(x):
		print(f"\nfound:\t{x}\t{x-1}\t{x-2}\t{x-3}\t")
		found = True
	else:
		print(f"{x}\t{x-1}\t{x-2}\t{x-3} does not match")
	x += 1


print(x-1)