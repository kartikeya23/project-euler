gt = 200
count = 0
for n200 in range(2):
	total = n200 * 200
	if total == 200:
		count += 1
	for n100 in range(int((200 - total) / 100) + 1):
		total = n100 * 100
		if total == 200:
			count += 1
		for n in xrange(1,10):
			pass