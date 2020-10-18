from datetime import datetime
start = datetime.now()

nums = 1

for x in range(7830457):
	nums *= 2
	nums %= int(1e10)

nums *= 28433
nums %= int(1e10)
nums += 1

print(nums)

print(f"\n\n\nfin in {datetime.now()-start}")
