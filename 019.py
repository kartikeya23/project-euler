months = {
	1: 3,
	2: 0,
	3: 3,
	4: 2,
	5: 3,
	6: 2,
	7: 3,
	8: 3,
	9: 2,
	10: 3,
	11: 2,
	12: 3
}

off = 2
count = 0
for y in range(1901, 2001):
	for m in range(1, 13):
		off = off + months[m]
		if y % 4 == 0 and m == 2:
			off += 1
		off %= 7
		if off == 0:
			count += 1

print(count)
