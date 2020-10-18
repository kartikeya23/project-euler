def fib(n):
	if n == 2:
		return 1
	elif n == 1:
		return 1
	return fib(n-1) + fib(n-2)

fib_1 = 1
curr = 2
index = 3
while len(str(curr)) < 1000:
	curr += fib_1
	fib_1 = curr - fib_1
	index += 1
	print(f"{index}\t\t{curr}")

print(f"\n\n n={index} \t\t {curr}")