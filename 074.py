from datetime import datetime
start = datetime.now()

from helper import getDgts, fact

def getNext(n):
	return sum([fact(x) for x in getDgts(n)])


top = 1e6
x = 69
ans_count = 0
while x < top:
	y = getNext(x)
	prev = [x]
	count = 1
	while y not in prev:
		count += 1
		prev.append(y)
		y = getNext(y)
	print(f"{x}\t\t\t\t{count}\n" + "----X" * 5)
	if count == 60:
		ans_count += 1
	x += 1


print(f"ans: {ans_count}")
print(f"\n\n\nfin in {datetime.now() - start}")
