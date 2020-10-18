from decimal import Decimal, getcontext
getcontext().prec = 101
tot = 0
for i in range(1, 101):
	rt = Decimal(i).sqrt()
	if rt % 1:
		s = sum([int(x) for x in str(rt).replace('.', '')[:-1]])
		tot += s
		print(rt, s, "y")
	else:
		print(rt, 'n')
print(tot)