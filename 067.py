from datetime import datetime
start = datetime.now()

tri = list(map(lambda a: list(map(int, a.split(" "))), open('p067_triangle.txt', 'r').readlines()))

print(tri)

iters = 0
for i in range(len(tri) - 2, -1, -1):
	for j in range(len(tri[i])):
		tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])
		iters += 1


print(f'after {iters} iterations found {tri[0][0]}')

print(f"\n\nfin in {datetime.now()-start}")



