'''
swea 5521. 상원이의 생일파티 D5
'''

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    g = [[0 for _ in range(N)] for _ in range(N)]
    res = 0
    v = [0] * N
    for i in range(M):
        s, e = map(int, input().split())
        g[s - 1][e - 1] = 1
        g[e - 1][s - 1] = 1

    for i in range(1, N):
        if g[0][i] == 1:
            if not v[i]:
                v[i] = 1
                res += 1
            for j in range(1, N):
                if g[i][j] == 1 and not v[j]:
                    v[j] = 1
                    res += 1
    print('#{} {}'.format(T, res))