def nton(n):
	x = n
	for i in range(1, n):
		x *= n
		x %= 10000000000
	return x

n = 1
s = 0
while n <= 1000:
	s += nton(n)
	s %= 10000000000
	n += 1

print(s)