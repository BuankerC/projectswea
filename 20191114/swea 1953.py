'''
swea 1953. [모의 SW 역량테스트] 탈주범 검거
'''
from collections import deque

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
PIPE = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
IN = [1, 0, 3, 2]

q = deque()
for T in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    D = [[-1 for _ in range(M)] for _ in range(N)]
    q.clear()
    q.append((R, C))
    D[R][C] = 0
    result = 1
    while len(q):
        x, y = q.popleft()
        p = data[x][y]
        for i in PIPE[p]:
            dx, dy = dxy[i]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and IN[i] in PIPE[data[nx][ny]] and D[nx][ny] == -1 and data[nx][ny] != 0:
                D[nx][ny] = D[x][y] + 1
                q.append((nx, ny))
                if D[nx][ny] < L:
                    result += 1
    print('#{} {}'. format(T, result))