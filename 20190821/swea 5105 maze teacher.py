def bfs(i, j, N):
    global maze
    #초기화
    q = []
    visited = [[0]*N for _ in range(N)]
    q.append([i, j]) # 시작점 인큐
    visited[i][j] = 1 # 시작점 방문표시

    #탐색
    while(len(q) != 0): # 큐가 비어있지 않으면 반복
        n = q.pop(o) #디큐
        i, j = n[0], n[1]
        if maze[i][j] == 3: #visit()
            return visited[i][j] - 2
        # i,j에 인접하고 방문하지 않은 칸을 인큐
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni >= 0 and ni < N and nj >= 0 and nj < 0 # 미로를 벗어나지 않았고
                if maze[ni][nj] != 1 and visited[ni][nj] == 0: # 벽이 아니고, 방문하지 않은 칸이면
                    q.append([ni, nj]) # 인큐
                    visited[ni][nj] = visited[i][j] # 방문 표시
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    startI = 0
    startJ = 0
    for i in range(N):
        for j in range(J):
            if maze[i][j] == '2':
                startI = i
                startJ = j
    print('#{} {}'.format(tc, bfs(startI, startJ, N)))