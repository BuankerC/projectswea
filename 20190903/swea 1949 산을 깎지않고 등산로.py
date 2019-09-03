def f(i, j, e):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    global N
    global maxV
    # 방문한 칸에 대해
    if maxV < e:  # 방문 칸을 포함한 등산로의 최대길이 비교
        maxV = e
    # 주변 칸을 탐색
    for m in range(4):
        ni = i + di[m]
        nj = j + dj[m]
        if ni >= 0 and ni < N and nj >= 0 and nj < N:  # 유효 좌표인지 확인
            if arr[i][j] > arr[ni][nj]:
                f(ni, nj, e + 1) # 주변의 낮은 칸으로 이동


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    h = 0 # 등산로의 시작 높이 설정
    for i in range(N):
        for j in range(N):
            if h < arr[i][j]:
                h = arr[i][j]
    maxV = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j]==h:
                f(i, j, 1) # 좌표 i, j, 남은 깍음 횟수, 등산로 길이
    print('#{} {}'.format(tc, maxV))