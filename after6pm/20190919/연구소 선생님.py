def bfs(lab, N, M):
    global maxV
    # 큐 생성
    # visited 생성
    # 시작점 인큐 및 visited 표시
    # 큐가 비어있지 않으면 반복
        # 디큐
        # 인접하고 방문하지 않은 곳이면 인큐 및 visited 표시

    # 모든 칸에 대해 lab[i][j]와 visited[i][j]가 0인 칸 수를 maxV와 비교
    

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
for i in range(N * M - 2):
    if lab[i // M][i % M] == 0:
        for j in range(i + 1, N * M - 1):
            if lab[j // M][j % M] == 0:
                for k in range(j + 1, N * M):
                    if lab[k // M][j % M] == 0:
                        lab[i // M][i % M] = 1
                        lab[j // M][j % M] = 1
                        lab[k // M][j % M] = 1
                        bfs(lab, N, M)
                        lab[i // M][i % M] = 0
                        lab[j // M][j % M] = 0
                        lab[k // M][j % M] = 0