from datetime import datetime
start = datetime.now()

x = 1
for i in range(1855):
	x = pow(1777, x, 10**8)

print(x)

print(f"\n\nfininshed in {datetime.now() - start}.")