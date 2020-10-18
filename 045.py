from datetime import datetime

start = datetime.now()

from math import sqrt

# def checkTri(n):
# 	for x in range(n):
# 		if n == (x+1) * x / 2:
# 			return True
# 	return False

def checkPent(n):
	x = (sqrt(24 * n + 1) + 1) / 6
	return x.is_integer()

def checkHex(n):
	x = (sqrt(8 * n + 1) + 1) / 4
	return x.is_integer()

found = False
x = 40755 + 286
d = 287
while not found:
	if checkPent(x):
		if checkHex(x):
			print(x)
			break
		else:
			print(f"{x} not hex")
	else:
		print(f"{x} not pent")
	x += d
	d += 1

print(f"finished in {datetime.now() - start}")
