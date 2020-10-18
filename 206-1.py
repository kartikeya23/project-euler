def check(num):
	s = str(num)
	c = 1
	for x in range(19):
		if x % 2 == 0:
			if s[x] != str(c):
				return False
			c = (c + 1) % 10

x = int(1e9)
y = x ** 2
while not check(y) and len(str(y)) == 19:
	print(f"{x}\t\t\t{y}")
	x += 10
	y = x ** 2

print(x - 1)