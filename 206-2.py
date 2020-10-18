from datetime import datetime
start = datetime.now()

from math import sqrt
from itertools import product

def join(nums):
	k = 1
	res = 0
	for x in range(17):
		res *= 10
		if x % 2 == 0:
			res += k
			k = (k + 1) % 10
		else:
			res += nums[x // 2]
	return res * 100


def isSquare(num):
	s = round(sqrt(num))
	return s ** 2 == num


n = [i for i in range(10)]
for x in product(n , repeat=8):
	number = join(list(x))
	s = sqrt(number)
	if isSquare(number):
		# print("--x--"*4 + "\n" + number)
		break
	print(f"{number}")

print(f"ans: {number}")

print("\n\nfin in {}".format(datetime.now() - start))