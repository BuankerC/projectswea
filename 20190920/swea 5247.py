'''
swea 5247 [파이썬 S/W 문제해결 구현] 6일차 - 연산 D4
'''

def bfs(n, m):
    f = r = -1
    v = {n: 1}
    r += 1
    q[r] = n
    while f != r:
        f += 1
        n = q[f]
        t = [n - 10, n - 1, n + 1, n * 2]
        for i in range(4):
            if t[i] == m:
                #print(v)
                return v[n]
            if 0 < t[i] <= min(1000000, M + 10):
                if not v.get(t[i]):
                    v[t[i]] = v[n] + 1
                    r += 1
                    q[r] = t[i]

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    q = [0] * 1000000
    r = bfs(N, M)
    print('#{} {}'.format(tc, r))