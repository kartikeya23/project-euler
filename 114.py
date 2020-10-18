from datetime import datetime
start = datetime.now()

facts = dict()

def fact(x):
	global facts
	if x <= 1:
		return 1
	if x in facts:
		return facts[x]
	f = x * fact(x-1)
	facts[x] = f
	return f

top = 50

tot = 1
b = top - 3
while b >= 0:
	x = fact(b+1) // fact(b)
	print(f"b={b}\t\t{top - b}\t\t{x}")
	tot += x
	b -= 1
print("using only one block: {}".format(tot))

b = 1
x = top - 6
while b <= x:
	y = (x - b + 1)
	tot += y
	print(f"b={b}\t\t{y}")
	b += 1

print(tot)

print(f"\n\n\nfin in {datetime.now()-start}")
