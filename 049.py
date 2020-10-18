from datetime import datetime

start = datetime.now()

def check(s):
	if (getd(s[:4]) == getd(s[4:8])) and (getd(s[-4:]) == getd(s[4:8])):
		return True
	return False

def getd(s):
	d = set()
	# print(s)
	for x in s:
		d.add(int(x))
	# if len(d) == 4:
	# 	return True
	return d

def isPrime(n):
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

p = list()

for x in range(1000, 10000):
	if isPrime(x):
		p.append(x)

l = len(p)
fir = 0
while fir < l:
	sec = fir + 1
	# print(f"f={fir}")
	while sec < l:
		third = 2 * p[sec] - p[fir] 
		if third in p:
			res = f"{p[fir]}{p[sec]}{third}"
			if check(res):
				print(res)
			# else:
				# print(f"found {res} but failed check")
		sec += 1
	fir += 1

fin = datetime.now()
print(f"\n\n\nfinished in {fin-start}")