'''
swea 5653. [모의 SW 역량테스트] 줄기세포배양
'''

from collections import deque

def my_func(n):
    new.clear()
    while len(q[n]):
        x, y = q[n].popleft()
        if timer[x][y] == life[x][y]:
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(life) and 0 <= ny < len(life[0]):
                    if life[nx][ny] == 0:
                        life[nx][ny] = life[x][y]
                        timer[nx][ny] = life[nx][ny] * 2
                        new.add((nx, ny))
                    elif life[nx][ny] < life[x][y] and (nx, ny) in new:
                        life[nx][ny] = life[x][y]
                        timer[nx][ny] = life[nx][ny] * 2
        if timer[x][y] > 0:
            timer[x][y] -= 1
        if timer[x][y] > 0:
            q[1 - n].append((x, y))
    for micro in new:
        q[1 - n].append(micro)

dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
q = [deque(), deque()]
for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    life = [[0 for _ in range(M + K + 1)] for _ in range(N + K + 1)]
    timer = [[0 for _ in range(M + K + 1)] for _ in range(N + K + 1)]
    q[0].clear()
    q[1].clear()
    tx = K // 2 + 1
    ty = K // 2 + 1
    for i in range(N):
        inputs = list(map(int, input().split()))
        for j in range(M):
            if inputs[j] != 0:
                x, y = i + tx, j + ty
                life[x][y] = inputs[j]
                timer[x][y] = inputs[j] * 2
                q[0].append((x, y))
    new = set()
    time = 0
    while True:
        my_func(0)
        time += 1
        if time >= K:
            break
        my_func(1)
        time += 1
        if time >= K:
            break
    result = 0
    for i in range(len(timer)):
        for j in range(len(timer[0])):
            if timer[i][j] != 0:
                result += 1
    print('#{} {}'.format(T, result))