T = int(input())
for case in range(1, T+1):
	size = int(input())
	triangle = [[] for i in range(size)]
	print(f'#{case}')
	for i in range(size):
		for j in range(i+1):
			if j == 0 or j == i:
				triangle[i].append(1)
			else:
				triangle[i].append(triangle[i-1][j-1] + triangle[i-1][j])
		result = " ".join(list(map(str, triangle[i])))
		print(f'{result}')