from datetime import datetime
start = datetime.now()

from helper import fib

const = int(1e9+7)

all_s = dict()
def s(n):
	try:
		return all_s[n]
	except:
		x = n // 9
		y = str(n % 9)
		all_s[x] = int(y + "9" * x) % const
		return all_s[x]


tot = 0
for x in range(2, 91):
	f = fib(x)
	t = 0
	for y in range(1, f + 1):
		t = (t + s(y)) & const
	print(f"{x}\t\t\t{f}\t\t\t{t}")



print("\ntot: {}".format(total))

print(f"\n\n\nfin in {datetime.now()-start}")
