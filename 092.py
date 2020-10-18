from datetime import datetime
start = datetime.now()

def getDgts(num):
	return sorted(list(map(int,str(num))))


def getNext(num):
	global to89
	global to1
	if num in to89:
		return 89
	elif num in to1:
		return 1
	tot = 0
	for x in getDgts(num):
		tot += x ** 2
	return int(tot)


to89 = set()
to1 = set()
top = 1e7
x = 1
match = 0
while x < top:
	y = x
	count = 0
	this = set([y])
	while not (y == 89 or y == 1):
		y = getNext(y)
		this.add(y)
		count += 1
	print(f"{x} reached {y}")
	if y == 1:
		to1.update(this)
	if y == 89:
		match += 1
		to89.update(this)
	x += 1

print(f"found: {match}")
print(f"\n\n\nfin in {datetime.now()-start}")