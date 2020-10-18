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


def red(p):
	tot = 0
	r = 1
	b = p - 2
	while b >= 0:
		tot += fact(b + r) // (fact(b) * fact(r))
		b -= 2
		r += 1
	return tot


def green(p):
	tot = 0
	g = 1
	b = p - 3
	while b >= 0:
		tot += fact(b + g) // (fact(b) * fact(g))
		b -= 3
		g += 1
	return tot



def blue(p):
	tot = 0
	bl = 1
	b = p - 4
	while b >= 0:
		tot += fact(b + bl) // (fact(b) * fact(bl))
		b -= 4
		bl += 1
	return tot


print(f"\n\n\nfin in {datetime.now()-start}")
