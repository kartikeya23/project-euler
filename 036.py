def bin(num):
	res = str()
	while num > 0:
		res += str(num % 2)
		num //= 2
	return res[::-1]

def chkPal(num):
	n = str(num)
	l = len(n)
	for i in range(l // 2 + 1):
		if n[i] != n[l-i-1]:
			return False
	return True

tot = 0
for x in range(1, int(1e6) + 1):
	if chkPal(x) and chkPal(bin(x)):
		tot += x
		print(f"dec: {x}\t\tbin: {bin(x)}")

print("\n\n" + str(tot))