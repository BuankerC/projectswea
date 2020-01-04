# 백준 15683, 감시

def f(n, k, N, M):
    global minV
    if n == k:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if office[i][j] == 0:
                    cnt += 1
        if cnt < minV:
            minV = cnt
    else:
        r, c, d = cctv[n]
        for m in cam[d]:
            watch = []
            for x in m:
                nr = r
                nc = c
                while 0 <= nr < N and 0 <= nc < M and office[nr][nc] != 6:
                    if office[nr][nc] == 0:
                        watch.append((nr, nc))
                        office[nr][nc] = 7
                    nr += dr[x]
                    nc += dc[x]
            f(n+1, k, N, M)
            for y in watch:
                office[y[0]][y[1]] = 0

cam = [[[0], [1], [2], [3]],
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]],
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
        [[0, 1, 2, 3]]]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]
cctv = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctv.append((i, j, office[i][j] - 1))
minV = 1000
f(0, len(cctv), N, M)
print(minV)