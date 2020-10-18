from datetime import datetime
start = datetime.now()

from itertools import permutations

nums = [str(i) for i in range(10)]
pans = list(map(lambda a: "".join(a), permutations(nums)))

primes = [2, 3, 5, 7, 11, 13, 17]
ans = list()
for n in pans:
	if n[0] is not '0':
		flag = True
		for off in range(1, 8):
			x = int(n[off:off+3])
			if x % primes[off-1] != 0:
				flag = False
		if flag:
			print(n)
			ans.append(int(n))

print(f"sum: {sum(ans)}")

print(f"finished in {datetime.now() - start}")
