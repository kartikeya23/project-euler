from datetime import datetime
start = datetime.now()

from math import log

f = open("p099_base_exp.txt", "r")

data = list()
count = 1
for l in f.readlines():
	n = [int(x) for x in l.split(",")]
	x = log(n[0]) * n[1]
	data.append((x, l, count))
	count += 1
	print(x)

	
data.sort(key=lambda a: a[0])
print(f"ans:{data[0]} \t\t\t{data[0][2]}")
print(f"ans:{data[-1]} \t\t\t{data[-1][2]}")


print(f"finished in {datetime.now() - start}")
