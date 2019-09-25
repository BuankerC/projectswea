

def defence(aw1, aw2, aw3, N, M, D):
    target = [[0] * M for _ in range(N)]
    hit = 0
    for i in range(N):
        for j in range(M):
            target[i][j] = enemy[i][j]
    for i in range(N):
        # 궁수와 거리가 D 이내에서 가장 가까운 적 중 맨 왼쪽의 적을 맞춤
        shoot(aw1, target, N, M, D)
        shoot(aw2, target, N, M, D)
        shoot(aw3, target, N, M, D)
        for r in range(N):  # 화살에 맞은 적을 가려냄
            for c in range(M):
                if target[r][c] > 1:
                    hit += 1
                    target[r][c] = 0
        for r in range(N - 1, 0 , -1):
            for c in range(M):
                target[r][c] = target[r - 1][c]  # 성벽 쪽으로 이동
        for c in range(0, M):
