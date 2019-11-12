'''
swea 1949. [모의 SW 역량테스트] 등산로 조성
'''
def f(i, j, c, e):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global N
    global K
    global maxV

    if maxV<e:
        maxV = e
    visited[i][j] = 1

    for m in range(4):
        ni = i + di[m]
        nj = j + dj[m]
        if ni>=0 and ni<N and nj>=0 and nj<N:
            if arr[i][j]>arr[ni][nj]:
                f(ni, nj, c, e+1)
            elif visited[ni][nj]==0 and c>0 and arr[i][j]>arr[ni][nj]-K:
                org = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1
                f(ni, nj, 0, e+1)
                arr[ni][nj] = org
    visited[i][j] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    h = 0
    for i in range(N):
        for j in range(N):
            if h<arr[i][j]:
                h = arr[i][j]

    maxV = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==h:
                f(i, j, 1, 1)

    print('#{} {}'.format(tc, maxV))