def isPrime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

primes = [2]

def r_to_l(n):
	global primes
	n //= 10
	while n > 0:
		if n not in primes:
			# print(f"\t\t{n} is not prime\tr_to_l")
			return False
		n //= 10
	return True
			
def l_to_r(n):
	global primes
	s = str(n)
	i = 0
	while i < len(s):
		if int(s[i:]) not in primes:
			return False
		i += 1
	return True


total = count = 0
x = 3
# for x in range(2, int(1e6)):
while count != 11:
	if isPrime(x):
		primes.append(x)
		if r_to_l(x) and l_to_r(x) and x > 7:
			total += x
			count += 1
			print(f"correctly found {x}")
		# else:
			# print(f"could only find prime: {x}")
	x += 2


print(f"\n\nfound {count} wiht a total of {total}")