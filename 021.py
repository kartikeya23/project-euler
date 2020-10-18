from datetime import datetime
start = datetime.now()

def factors(num):
	f = list()
	for x in range(1, int(num**0.5)+1):
		if num % x == 0:
			f.append(x)
			f.append(num // x)
	return sorted(f)


def d(num):
	return sum(factors(num)) - num



top = 10000
nums = set()
for a in range(top):
	b = d(a)
	if d(b) == a and a != b:
		nums.add(a)
		nums.add(b)
		print(f"pair:\t{a}\t\t\t{b}")

print(f"total is: {sum(nums)}")

print(f"\n\n\nfin in {datetime.now()-start}")
