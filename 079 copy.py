from datetime import datetime
start = datetime.now()

print("reading data from file")
file = open('p079_keylog.txt', 'r')
data = [int(l) for l in file.readlines()]

print(f"successful entries are: {data}\n\n")

def getallocc(s, c):
	l = len(s)
	res = list()
	for i in range(l):
		if s[i] == c:
			res.append(i)
	return res


def check(num, inp):
	inp = str(inp)
	num = str(num)
	x = [getallocc(num, d) for d in inp]
	for y in x:
		if len(y) == 0:
			return False
	mins = [min(y) for y in x]
	if x[0] < x[1] and x[1] < x[2]:
		return True
	return False


found = False
x = 100
while not found:
	x += 1
	found = True
	for c in data:
		found = found and check(x, c)
		if not found:
			print(f"error on:\t\t\t{x}")
			break

print(f"found answer:\t{x}\n\n\n")
print(f"\n\n\nfin in {datetime.now()-start}")