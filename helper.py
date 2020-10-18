from math import sqrt
from functools import reduce


primes = [2]
def isPrime(n):
	global primes
	if n in primes:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	primes.append(n)
	return True


def fib(n):
	if n <= 1:
		return n
	return fib(n-1) + fib(n-2)


def hcf(a, b):
	if a == 0:
		return b
	return hcf(b%a, a)


def factor_count(n):
  return len(factors(n))


def factors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


facts = dict()
def fact(n):
	global facts
	if n in facts:
		return sacts[n]
	if n <= 1:
		return 1
	x = n * fact(n - 1)
	facts[n] = x
	return x


def recLen(d):
	rems = list()
	x = 10 ** len(str(d))
	rem = x % d
	while rem not in rems:
		rems.append(rem)
		rem *= x
		rem %= d
	return len(rems) - rems.index(rem)


def isPal(num):
	n = str(num)
	l = len(n)
	for i in range(l // 2 + 1):
		if n[i] != n[l-i-1]:
			return False
	return True


def decToBin(num):
	res = str()
	while num > 0:
		res += str(num % 2)
		num //= 2
	return res[::-1]


def isPent(n):
	x = (sqrt(24 * n + 1) + 1) / 6
	return x.is_integer()


def isHex(n):
	x = (sqrt(8 * n + 1) + 1) / 4
	return x.is_integer()


def primeFactors(n):
	return [x for x in factors(n) if isPrime(x)]


def getDgts(n):
	return [int(x) for x in str(n)]


def dgtSum(n):
	return sum(getDgts(n))


# Euler's totient function
def phi(n):
	res = n
	p = 2
	while p <= sqrt(n):
		if n % p == 0:
			while n % p == 0:
				n //= p
			res *= (1 - 1 / p)
		p += 1
	if n > 1:
		res *= (1 - 1 / n)
	return int(res)
