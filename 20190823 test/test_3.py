def f(i, j, N):
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    global v
    v[i][j] = 1
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if ni >= and ni < N and nj >= 0 and nj < N:
            if v[ni][nj] == 0 and arr[ni][nj] > 0:
                f(ni, nj, N)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if (arr[i][j] > 0 and v[i][j] == 0):
                f(i, j, N)
                cnt = cnt + 1

    print('#{} {}'.format(tc, cnt))
