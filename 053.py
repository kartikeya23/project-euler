from datetime import datetime
start = datetime.now()

def fact(x):
	if x <= 1:
		return 1
	return x * fact(x-1)

def comb(n):
	r = n // 2
	return fact(n) / (fact(r) * fact(n-r))

count = 0
for x in range(1, 101):
	c = comb(x)
	print(f"n={x}\t\t\t{c}")
	if c > 1e6:
		count += 1
		print("matches condition")

print(f"\n\nfound a total of{count}\n\n")

print(f"fin in {datetime.now() - start}")
