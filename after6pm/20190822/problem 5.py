T = int(input())
a = []
cnt = 0
A = map(int, input().split())
for i in range(1, i-2):
    for j in range(1, j-2):
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            a.append(A[ni][nj])
        if A[i][j] > max(a):
            cnt += 1