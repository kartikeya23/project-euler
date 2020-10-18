count = 0

def check(l):
	if l >= 0:
		global count
		count += 1
		print(f"found combination")
	else:
		print(f"\t\t\t\t\t\t{l}")

for n200 in range(2):
	left = 200 - n200 * 200
	check(left)
	for n100 in range(int(left / 100 + 1)):
		left -= n100 * 100
		check(left)
		for n50 in range(int(left / 50 + 1)):
			left -= n50 * 50
			check(left)
			for n20 in range(int(left / 20 + 1)):
				left -= n20 * 20
				check(left)
				for n10 in range(int(left / 10 + 1)):
					left -= n10 * 10
					check(left)
					for n5 in range(int(left / 5 + 1)):
						left -= n5 * 5
						check(left)
						for n2 in range(int(left / 2 + 1)):
							left -= n2 * 2
							if not left < 0:
								check(left)

							
