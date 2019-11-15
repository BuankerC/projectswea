'''
swea 2105. [모의 SW 역량테스트] 디저트 카페
'''

dxy = [[1, 1], [1, -1], [-1, -1], [-1, 1]]

def dfs(x, y, d, cnt):
    for i in range(d, d + 2):
        if i >= len(dxy):
            continue
        nx, ny = x + dxy[i][0], y + dxy[i][1]
        if 0 <= nx < N and 0 <= ny < N:
            if not taken[data[nx][ny]] and not visited[nx][ny]:
                taken[data[nx][ny]] = True
                visited[nx][ny] = 1
                dfs(nx, ny, i, cnt + 1)
                visited[nx][ny] = 0
                taken[data[nx][ny]] = False
            elif nx == start[0] and ny == start[1] and cnt >= 3:
                global result
                result = max(result, cnt + 1)

for T in range(1, int(input()) + 1):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    result = -1
    taken = [False for _ in range(101)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N - 2):
        for j in range(1, N - 1):
            start = (i, j)
            taken[data[i][j]] = True
            visited[i][j] = 1
            dfs(i, j, 0, 0)
            taken[data[i][j]] = False
            visited[i][j] = 0
    print('#{} {}'.format(T, result))