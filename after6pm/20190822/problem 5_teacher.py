di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]


def f(i, j):
    global A

    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if A[i][j] <= A[ni][nj]:
            return 0
    return 1

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for i in range(1, N-1):
    for j in range(1, N-1):
        # cnt += f(j, j)
        s = []
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            s.append(A[ni][nj])
        if A[i][j] > max(s):
            cnt += 1
print(cnt)