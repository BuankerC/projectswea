'''
swea 4615. 재미잇는 오셀로 게임 D3
'''
def is_not_limit(a, b, n):
    if a >= 0 and a < n and b >= 0 and b < n:
        return True
    else:
        return False

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    data = [[0] * N for _ in range(N)]
    data[N // 2 - 1][N // 2] = 1
    data[N // 2][N // 2 - 1] = 1
    data[N // 2 - 1][N // 2 - 1] = 2
    data[N // 2][N // 2] = 2

    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]

    for _ in range(M):
        a, b, stone = map(int, input().split())
        x = a - 1
        y = b - 1
        data[x][y] = stone
        for i in range(8):
            cnt = 0
            next_x = x + dx[i]
            next_y = y + dy[i]
            while is_not_limit(next_x, next_y, N) and stone != data[next_x][next_y] and data[next_x][next_y] != 0:
                cnt += 1
                next_x = next_x + dx[i]
                next_y = next_y + dy[i]

            if is_not_limit(next_x, next_y, N) and data[next_x][next_y] == stone:
                next_x = x + dx[i]
                next_y = y + dy[i]
                for f in range(cnt):
                    data[next_x][next_y] = stone
                    next_x = next_x + dx[i]
                    next_y = next_y + dy[i]

    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                cnt1 += 1
            elif data[i][j] == 2:
                cnt2 += 1
    print('#{} {} {}'.format(t, cnt1, cnt2))