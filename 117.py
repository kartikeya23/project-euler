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


r = 0
tot = 0
top = 50
while r <= top // 2:
	g = 0
	while g <= (top - 2 * r) // 3:
		bl = 0
		while bl <= (top - 2 * r - 3 * g) // 4:
			x = top - (2*r + 3*g + 4*bl)
			tot += fact(r+bl+g+x) / (fact(r) * fact(g) * fact(bl) * fact(x))
			print(tot)
			bl += 1
		g += 1
	r += 1


print("\n"*3, tot)

print(f"\n\n\nfin in {datetime.now()-start}")
