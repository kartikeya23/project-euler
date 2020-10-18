top = 28123

def checkAbd(n):
	sf = 0
	for i in range(1, n):
		if not n % i:
			sf += i
	if sf > n:
		print(f"found new abd number \t{n}\tsum of fact = {sf}")
		return True
	return False

abd = list()

for x in range(top):
	if checkAbd(x):
		abd.append(x)

abd_count = len(abd)

print(f"\n\nfound {abd_count} abundant numbers")

tot = 0
for x in range(12, top):
	flag = False
	for y in range(12, x):
		if y in abd and (x-y) in abd:
			flag = True
			break
	if not flag:
		print(f"cannot express {x}")
		tot += x

print(f"their total is {tot}")

# sums = list()

# print("finding sums now\n\n")

# for x in range(abd_count):
# 	for y in range(x, abd_count):
# 		sums.append(abd[x] + abd[y])

# print("\n")

# tot = 0
# allnum = list(range(top))
# for x in sums:
# 	if x > top:
# 		break
# 	allnum.remove(x)

# print(f"the sum of all numbers is {sum(allnum)}")


# print(f"\n\nthe sum is {tot}")