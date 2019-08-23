T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N)]

    for k in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        for i in range(x1, x2 + 1): #일곱 영역의 행
            for j in range(y1, y2 + 1): #일곱 영역의 열
                arr[i][j] = 1

    cnt = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 1:
                cnt += 1
    print('#{} {}'.format(tc, cnt))
