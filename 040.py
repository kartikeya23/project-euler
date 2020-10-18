s = " "

for x in range(1, 10000000):
	s += str(x)

p = 1
for y	in range(7):
	p *= int(s[10 ** y])

print(p)