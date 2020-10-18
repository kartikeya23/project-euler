x = int(1e9)
y = x ** 2
dgt = 2
at = 2
while dgt != 1:
	while str(y)[at] != dgt:
		x += 10
		y = x ** 2
		print(f"x={x}\t\t\t\ty={y}")
	print(f"x={x}\t\t\t\ty={y}")
	at += 2
	dgt = (dgt + 1) % 10


print(x - 1)