from datetime import datetime
start = datetime.now()

k = 2
leading = 1
coeffs = [1, 2]
for i in range(97):
	if (i + 1) % 3 == 0:
		coeffs.append(k)
		k += 2
	else:
		coeffs.append(1)

print(f"the coeffs are: {coeffs}")

# i = 98
# num = 0
# denom = 1
# while i >= 0:
# 	tmp = num
# 	num = denom
# 	denom = denom * coeffs[i] + tmp
# 	print(f"{99-i}.\tn={num}\t\t\t/\t\t{denom}")
# 	i -= 1

at = 1
num = 0
denom = 1
while at < 100:
	tmp = num
	num = denom
	denom = coeffs[-1 * at] * denom + tmp
	print(f"{i}.\tn={num}\t\t\t/\t\t{denom}")
	at += 1



tmp = num
num = denom
denom = denom * leading + tmp

print(f"\n\n\n{num}\t\t\t/\t\t{denom}")

print(f"sum of digits of num = {sum(map(int, str(num)))}")

print(f"\n\n\nfin in{datetime.now()-start}")