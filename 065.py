coeffs = []
n = 2
while n <= 100:
	if n % 3:
		coeffs.append(1)
	else:
		coeffs.append(2 * n // 3)
	n += 1
# print(coeffs)
# print(len(coeffs))
c = coeffs[::-1]
print(c)
num = 1
denom = c[0]
for i in range(1, 99):
	tmp = denom * c[i] + num
	num = denom
	denom = tmp
print(num)
print(denom)
print(x := 2 * denom + num)
print(sum([int(i) for i in str(x)]))