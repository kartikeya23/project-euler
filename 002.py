def fib(n):
	if n <= 1:
		return 1
	return fib(n-1) + fib(n-2)

n = m = 1
tot = 0
while m < 4000000:
	if m % 2 == 0:
		tot += m
		print(f"added {m}")
	n += 1
	m = fib(n)
print(tot)