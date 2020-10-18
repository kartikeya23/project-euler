last = 9
total = 25
side = 5

while side <= 1001:
	total += 4 * last + 10 * (side - 1)
	last += 4 * (side - 1)
	print(f"for s={side}\t\ttot={total}")
	side += 2

print(f"\n\n\nthe total is {total}")