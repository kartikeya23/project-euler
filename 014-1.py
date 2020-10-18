maxd = 0
at = -1
for x in range(1, int(1e6)):
	tmp = x
	count = 0
	print(f"checking {x}")
	while tmp != 1:
		count += 1
		if tmp % 2:
			tmp = tmp * 3 + 1
		else:
			tmp /= 2
	if maxd < count:
		at = x
		maxd = count

print(f"max at n={at}\t\t{maxd}")