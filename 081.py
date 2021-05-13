from datetime import datetime
start = datetime.now()

data = open('p081_matrix.txt', 'r').read()
mat = [list(map(int, x.split(','))) for x in data.splitlines()]

n = len(mat) - 1

for i in range(n-1, -1, -1):
	mat[i][n] += mat[i+1][n]
	mat[n][i] += mat[n][i+1]

for i in range(n-1, -1, -1):
	for j in range(n-1, -1, -1):
		mat[i][j] += min(mat[i+1][j], mat[i][j+1])
	
print(mat[0][0])


print(f"\n\nfininshed in {datetime.now() - start}.")