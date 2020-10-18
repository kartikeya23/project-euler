s = set()

for a in range(2, 101):
	for b in range(2, 101):
		s.add(a**b)

print(s, end="\n\n")
print(len(s))