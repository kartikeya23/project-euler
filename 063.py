from datetime import datetime
start = datetime.now()

def nd(num):
	c = 0
	while num > 0:
		c += 1
		num //= 10
	return c

count = 1
for x in range(1, 100):
	for y in range(2, 11):
		if nd(y**x) == x:
			print(f"{x}\t\t\t{y}")
			count += 1

print("found {}".format(count))

print(f"\n\n\nfin in {datetime.now()-start}")