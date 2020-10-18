from datetime import datetime
start = datetime.now()

num = 3
denom = 2
d_last = 1
n_last = 1
ans_count = 0
for x in range(2, 1001):
	num = 2 * num + n_last
	n_last = (num - n_last) // 2
	denom = 2 * denom + d_last
	d_last = (denom - d_last) // 2
	print(f"{x}.\t\t\t{num}\t\t\t/\t\t\t{denom} = {num/denom}")
	if len(str(num)) > len(str(denom)):
		ans_count += 1


print(f"ans: {ans_count}")
print(f"\n\n\nfin in {datetime.now() - start}")
