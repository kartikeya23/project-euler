def isPrime(n):
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

u_bound = int(1e6)
primes = list()

for x in range(2, u_bound):
	if isPrime(x):
		primes.append(x)

lmax = l = 22
top = 0

while sum(primes[:l]) < u_bound and l < len(primes):
	print(f"checking with l={l}")
	start = 0
	s = sum(primes[start:start+l])
	while start < (len(primes) - l) and s < u_bound:
		s = sum(primes[start:start+l])
		if s in primes:
			lmax = l
			top = s
			print("found streak of {}: {}\nwith sum {}\n\n".format(l, primes[start:start+l], s))
			break
		else:
			print(f"{s} is not prime")
		start += 1
	l += 1


print(lmax)