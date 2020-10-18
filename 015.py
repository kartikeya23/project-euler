def find_paths(x):
	c = 1
	for i in range(1, x + 1):
		c *= (x + i) / i
	return c

