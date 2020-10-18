def fact(x):
	if x == 0 or x == 1:
		return 1
	return x * fact(x-1)

f = []
for x in range(10):
	f.append(fact(x))
print(f)

def gdfs(n):
	tot = 0
	for d in str(n):
		tot += f[int(d)]
	return tot

total = 0
for x in range(3, int(1e5)):
	if x == gdfs(x):
		print(x)
		total += x

print(f"their total is {total}")