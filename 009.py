import math

for a in range(1, 1000):
	for b in range(a + 1, 1000 - a):
		c1 = 1000 - (a + b)
		c2 = math.sqrt(a ** 2 + b ** 2)
		if c1 == c2:
			print(f"a={a}\tb={b}\tc={c1}")
			