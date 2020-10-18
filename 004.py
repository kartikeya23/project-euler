high = 0
for x in range(999, 99, -1):
	for y in range(999, 99, -1):
		n = x * y
		print(n)
		if str(n) == str(n)[::-1]:
			if n > high:
				high = n

print(high)