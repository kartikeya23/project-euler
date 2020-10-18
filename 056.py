from datetime import datetime

start = datetime.now()

def getDgtSum(num):
	return sum(list(map(int, str(num))))

maxsum = 0
for a in range(100):
	for b in range(100):
		x = a ** b
		# print(x)
		maxsum = max([maxsum, getDgtSum(x)])

print(f"the max power digit sum is {maxsum}\n\n")
print(f"fin in {datetime.now()-start}")