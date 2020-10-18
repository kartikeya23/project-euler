class Depths():
	def __init__(self):
		self.memo = []

	def add(self, n, d):
		self.memo.append((n, d))

	def find(self, n):
		for x in self.memo:
			if x[0] == n:
				return True
		return False
		
	def get(self, n):
		for x in self.memo:
			if x[0] == n:
				return x[1]
		
dp = Depths()

def seq(it=0, n=2):
	it += 1
	if n == 1:
		return it
	if dp.find(n):
		return it + dp.get(n)
	if not n % 2:
		tmp = seq(it, n / 2)
	else:
		tmp = seq(it, 3 * n + 1)
	dp.add(n, tmp)
	return tmp

high = seq()
at = 2
for n in range(int(1e6)):
	chain = seq(n=n)
	if chain > high:
		high = chain
		at = n

print(f"max at n = {at}\t\t {high}")
