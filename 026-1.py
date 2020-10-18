from datetime import datetime
start = datetime.now()

longest = 0
for x in range(1000):
	if x % 2 == 0 or x % 5 == 0:
		continue
	rec = 1 / x
	d = 1
	off = 10 ** d
	y = rec * off - rec
	while not y.is_integer():
		d += 1
		off = 10 ** d
		y = rec * off - rec
	if d > longest:
		longest = d
		print(f"1 / {x}\t\t{d}")

print(longest)

print(f"\n\n\nfin in {datetime.now()-start}")
