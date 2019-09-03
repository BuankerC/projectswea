def f(i, j, N):  # i, j 좌표, e 지나온 칸 수, N 미로의 크기
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    global minV
    if maze[i][j] == 3:  # 도착지면
        if minV > e:
            minV = e
    else:  # 도착지가 아니면
        maze[i][j] = 1  # 현재 칸에 방문 표시(진행 방향에서 다시 들어오는 것 방지)
        for k in range(4):  # 이동 가능한 칸으로 이동
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < N:  # 미로를 벗어나지 않고
                if maze[ni][nj] != 1:  # 갈 수 있는 칸이면(벽이 아니면)
                    f(ni, nj, e+1, N)
        maze[i][j] = 1  # 새로운 경로롤 현재 칸에 진입 허용

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in range()] for i in range(N)] # 미로를 중첩리스트로 저장
    for i in range(N):
        if 2 in maze[i]:
            sRow = i                # 출발 row index
            sCol = maze[i].index(2) # 출발 column index
    minV = 1000000000
    f(sRow, sCol, 0, N)  # 미로 탐색
    if minV == 1000000000:
        minV = 1
    print('#{} {}'.format(tc, minV))