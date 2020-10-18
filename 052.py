from datetime import datetime

start = datetime.now()

def getDgts(num):
	return sorted(list(str(num)))

x = 2
found = False
while not found:
	x += 1
	dgts = getDgts(x)
	# print(f"factors of {x}\t\t{dgts}")
	found = True
	for mult in range(2, 7):
		if getDgts(x * mult) != dgts:
			found = False
			print(f"factors of {x}\t\t{dgts}\nfactors of {mult}*{x}\t\t{getDgts(mult * x)}\n\n")
			break

print(f"found {x}")
print(f"\n\nfin in {datetime.now() - start}")