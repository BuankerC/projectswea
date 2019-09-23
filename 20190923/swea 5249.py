'''
swea 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리 D4
'''
def MST(s, n):
    global INF
    dist[s] = 0

    for i in range(n):
        u = get_min_vertext(n)
        visited[u] = True

        if dist[u] == INF:
            return

        for v in range(n):
            if g[u][v] != INF:
                if not visited[v] and g[u][v] < dist[v]:
                    dist[v] = g[u][v]


def get_min_vertext(n):
    v = 0
    for i in range(n):
        if not visited[i]:
            v = i
            break

    for j in range(n):
        if not visited[j] and dist[j] < dist[v]:
            v = j
    return v



for TC in range(1, int(input())+1):
    INF = 987654321
    V, E = map(int, input().split())
    g = [[INF for _ in range(V+1)] for _ in range(V+1)]
    visited = [False]*(V+1)
    dist = [INF]*(V+1)


    for _ in range(E):
        s, e, d = map(int, input().split())
        g[s][e] = d
        g[e][s] = d
    MST(0, V+1)
    print('#{} {}'.format(TC, sum(dist)))