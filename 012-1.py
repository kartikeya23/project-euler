import math

def factor_count(n):
	count = 1
	while not n % 2:
		count += 1
		n  /= 2
	for i in range(3, int(math.sqrt(n)) + 1, 2): 
		c = 1
		while n % i == 0:
			n /= i
			c += 1
		if c == 1:
			count += 1
		else:
			count *= c
	return count

num = 1
count = 2
fac = factor_count(num)
while fac <= 500:
	print(f"{num} only has {fac} factors")
	num += count
	count += 1
	fac = factor_count(num)

print(f"\n\nthe {count - 1}th triangular number {num} has {fac} factors")
