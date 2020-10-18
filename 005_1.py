def hcf(a, b):
	if a == 0:
		return b
	return hcf(b%a, a)

lcm = 2
for i in range(2, 21):
	lcm = (lcm * i) / hcf(lcm, i)

print(lcm)