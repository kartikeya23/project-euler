arr = [0, 0, 1, 2]
for n in range(4, 101):
	arr.append(round((n-1)/2) + arr[n-1])

for i, x in enumerate(arr):
	print(i, x)

