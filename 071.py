from math import gcd, floor
from datetime import datetime

start = datetime.now()

target = 3/7
res = 0
ans = (0, 0)
for d in range(1, 1000001):
	n = floor(d * target)
	# print(n)
	if n / d > res and n / d < target:
		g = gcd(n, d)
		ans = (n // g, d // g)
		res = n / d
		print(n, d, ans)
print(ans)

print(f"fin in {datetime.now() - start}")