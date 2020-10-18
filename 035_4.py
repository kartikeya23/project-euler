from datetime import datetime
start = datetime.now()

from itertools import permutations

def isPrime(n):
	if n % 2 == 0:
		if n == 2:
			return True
		return False
	for i in range(3, int(n**0.5) + 1, 2):
		if n % i == 0:
			return False
	return True

def rotate(inp, d): 
	# slice string in two parts for left and right 
	Lfirst = inp[0 : d] 
	Lsecond = inp[d :]
	
	return int(Lsecond + Lfirst)

def prime(n):
	global p
	if isPrime(n):
		p.add(n)
		return True
	return False

high_bound = 1e6
x = 3
count = 0
p = set()
forbid = ['0', '2', '5', '6', '8', '4']
fin = set()
while x < high_bound:
	if prime(x):
		p.add(x)
		s = str(x)
		flag = True
		for c in s:
			if c in forbid:
				flag = False
				break
		if flag:
			check = True
			for d in range(len(s)):
				if not prime(rotate(s, d)):
					check = False
					break
			if check:
				count += 1
				fin.add(x)
	x += 2

print(f"found {count} items \n {sorted(fin)}\n\n")
print(f"fin in {datetime.now() - start}")
