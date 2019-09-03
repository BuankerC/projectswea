'''
swea 1949. [모의 sw 역량테스트] 등산로 조성
'''

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(x, y, use, leng):
    temp = leng
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            visited[nx][ny] = True
            if data[x][y] > data[nx][ny]:
                temp = max(temp, dfs(nx, ny, use, leng + 1))
            elif data[x][y] <= data[nx][ny] and not use and data[x][y] > data[nx][ny] - K:
                temp_height, data[nx][ny] = data[nx][ny], data[x][y] - 1
                temp = max(temp, dfs(nx, ny, True, leng + 1))
                data[nx][ny] = temp_height
            visited[nx][ny] = False
    return temp

for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    start = [0, set({})]
    for i in range(N):
        for j in range(N):
            if start[0] < data[i][j]:
                start[0] = data[i][j]
                start[1].clear()
                start[1].add((i, j))
            elif start[0] == data[i][j]:
                start[1].add((i, j))
    result = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for x, y in start[1]:
        visited[x][y] = True
        result = max(result, dfs(x, y, False, 1))
        visited[x][y] = False
    print('#{} {}'.format(T, result))
