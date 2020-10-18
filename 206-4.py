from datetime import datetime
start  = datetime.now()

def check(num):
	s = str(num)
	c = 1
	for x in range(19):
		if x % 2 == 0:
			if s[x] != str(c):
				return False
			c = (c + 1) % 10


def check2(num):
	s = str(num)
	for x in range(10):
		if s[2 * x] != str((x + 1) % 10):
			return False
	return True


x = int(1e9)
y = x ** 2
while not check2(y) and y <= 1929394959697989900:
	print(f"{x}\t\t\t{y}")
	x += 10
	y = x ** 2

print(x - 10)

print(f"\n\nfin in {datetime.now() - start}")