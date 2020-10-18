from datetime import datetime
start = datetime.now()

from helper import isPrime

found = False
x = 10
while not found:
	while not isPrime(x):
		

print(f"finished in {datetime.now() - start}")
