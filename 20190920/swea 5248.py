'''
swea 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기 D3
'''
def dfs(n):
    global N
    global res
    for i in range(N):
        if not V[i]:
            if g[n][i]:
                V[i] = 1
                dfs(i)

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    case = list(map(int, input().split()))
    res = 0
    g = [[0 for _ in range(N)] for _ in range(N)]
    V = [False] * N
    for i in range(0, len(case), 2):
        r = case[i] - 1
        c = case[i + 1] - 1
        g[r][c] = 1
        g[c][r] = 1

    for i in range(N):
        if not V[i]:
            res += 1
            dfs(i)
    print('#{} {}'.format(tc, res))