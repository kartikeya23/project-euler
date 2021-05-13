from datetime import datetime
start = datetime.now()

# top = int(1e14)
top = 10

S = 0
mod = int(1e9 + 7)

squares = [i**2 for i in range(1, 10000000)]

def g(x):
	i = 0
	while squares[i] <= x // 2:
		

for i in range(1, top):
	S += g(i)


print(f"\n\nfininshed in {datetime.now() - start}.")