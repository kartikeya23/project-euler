from datetime import datetime
start = datetime.now()

def f(n,d):
	n = str(n)
	d = str(d)
	if n[0] == n[1] or d[0] == d[1]:
		return 0
	for c in n:
		if c in d:
			return int(n.replace(str(c), '')) / int(d.replace(str(c), ''))
	return 0

n = 10
p = 1
while n < 99:
	d = n + 1
	while d < 100:
		if n%10 and d%10:
			if n/d == f(n, d):
				print(f"{n}\t\t{d}")
				p *= n / d
		d += 1
	n += 1
				

print(p, "\t"*3, p.as_integer_ratio())

print(f"\n\n\nfin in {datetime.now()-start}")
