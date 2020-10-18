from datetime import datetime
start = datetime.now()

from itertools import permutations

nums = [str(i) for i in range(1, 10)]
pans =list(map(lambda a: "".join(a), permutations(nums)))
succ = set()

print(F"finding 1, 4, 4")
for p in pans:
	x = int(p[0])
	y = int(p[1:5])
	z = int(p[5:])
	if z == x * y:
		print(F"{x}\t*\t{y}\t\t=\t{z}")
		succ.add(z)


print(F"finding 2, 3, 4")
for p in pans:
	x = int(p[:2])
	y = int(p[2:5])
	z = int(p[5:])
	if z == x * y:
		print(F"{x}\t*\t{y}\t\t=\t{z}")
		succ.add(z)

print(F"sum: {sum(succ)}")

print(f"finished in {datetime.now() - start}")
