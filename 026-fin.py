from datetime import datetime
start = datetime.now()

def recLen(d):
	rems = list()
	x = 10 ** len(str(d))
	rem = x % d
	while rem not in rems:
		rems.append(rem)
		rem *= x
		rem %= d
	return len(rems) - rems.index(rem)


maxl = 0
for x in range(1, 1000):
	if x%2 and x%5:
		y = recLen(x)
		print(f"1/{x}\t\t\t{y}")
		maxl = max(maxl, y)
		
print(maxl)

print(f"\n\n\nfin in {datetime.now()-start}")
