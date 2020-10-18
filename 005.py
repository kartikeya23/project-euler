found = False
x = 100
while not found:
	found = True
	for n in range(2, 21):
		if x % n != 0:
			found = False
			break
	x += 1
print(x)