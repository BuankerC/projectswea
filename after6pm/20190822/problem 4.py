T = int(input())
for i in range(1, i-2):
    for j in range(1, j-2):
        if A[i][j + 1] == 0 and A[i + 1][j] == 0 and A[i][j - 1] == 0 and A[i - 1][j] == 0:
            cnt += 1