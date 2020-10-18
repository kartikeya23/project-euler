from functools import reduce

def factor_count(n):
  return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

num = 1
count = 2
fac = factor_count(num)
while fac <= 500:
	print(f"{num} only has {fac} factors")
	num += count
	count += 1
	fac = factor_count(num)

print(f"\n\nthe {count - 1}th triangular number {num} has {fac} factors")
