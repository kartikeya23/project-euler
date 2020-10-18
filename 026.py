from datetime import datetime
start = datetime.now()

longest = 0
for x in range(1, 1001):
	y = 1 / x
	count = 1
	p = 10
	flag = False
	while not flag:
		flag = (y * p - y).is_integer()
		p *= 10
		count += 1
	if count > longest:
		longest = count

print(longest)
print(f"\n\nfin in {datetime.now()-start}")