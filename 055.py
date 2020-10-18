from datetime import datetime

start = datetime.now()

max_iter = 50
upper_bound = 1e4

def getRev(num):
	s = str(num)
	return int(s[::-1])

def rad(num):
	return num + getRev(num)

def isPal(num):
	n = str(num)
	l = len(n)
	for i in range(l // 2 + 1):
		if n[i] != n[l-i-1]:
			return False
	return True

x = 1
count = 0
while x < upper_bound:
	flag = False
	i = 0
	y = rad(x)
	while not flag and i < max_iter:
		flag = isPal(y)
		i += 1
		y = rad(y)
	if flag:
		print(f"{x} is a lychrel number w/ {i} iterations")
		count += 1
	else:
		print(f"{x} is not")
	x += 1	

print(f"\n\nfound {count} lychrel numbers\n\n")

print(f"fin in {datetime.now()-start}")