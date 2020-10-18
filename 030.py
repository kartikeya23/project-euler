def get_sum(n):
	t = 0
	for d in str(n):
		t += int(d) ** 5
	return t

spec = list()
for x in range(2, int(1e6)):
	# print("")
	if x == get_sum(x):
		print("found " + str(x))
		spec.append(x)

print(spec)
print(sum(spec))