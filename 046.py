from datetime import datetime
start = datetime.now()

from math import sqrt

p = list()
def isPrime(n):
	global p
	if n in p:
		return True
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	p.append(n)
	return True


x = 1
flag = True
while flag:
	x += 2
	if not isPrime(x):
		flag = False
		for y in range(int(sqrt(x))):
			z = x - 2 * y ** 2
			if z > 0 and isPrime(z):
				print(f"{x}\t\t=\t\t{z}\t\t+\t\t2 * {y} \t\t^ 2")
				flag = True
				break

print(f"ans: {x}")


print(f"finished in {datetime.now() - start}")
