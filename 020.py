def fact(n):
	if n == 1:
		return 1
	return n * fact(n-1)

f = fact(100)
print(f)
tot = 0
for d in str(f):
	tot += int(d)

print(tot)