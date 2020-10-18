def checkTotal(n_1, n_2, n_5, n_10, n_20, n_50, n_100, n_200):
	total = n_1
	total += n_2 * 2
	total += n_5 * 5
	total += n_10 * 10
	total += n_20 * 20
	total += n_50 * 50
	total += n_100 * 100
	total += n_200 * 200
	if total == 200:
		return True
	return False

count = 0

tot = 0
for n200 in range(2):
	tot = n200 * 200
	if tot < 200:
		for n100 in range(3):
			tot += n100 * 100
			if tot < 100:
				for n50 in range(5):
					tot += n50 * 50
					if tot < 200:
						for n20 in range(11):
							tot += n20 * 20
							if tot < 200:
								for n10 in range(21):
									tot += n10 * 10
									if tot < 200:
										for n5 in range(41):
											tot += 
											if tot < 200:
												for n2 in range(101):
													if tot < 200:
														count += 1
														print(f"{n1}\t{n2}\t{n5}\t{n10}\t{n20}\t{n50}\t{n100}\t{n200}")
					elif tot == 200
						count += 1
			elif tot == 200
				count += 1
	elif tot == 200
		count += 1