'''
swea 7465 .
창용 마을 무리의 개수 D4
'''

def rep(n):
    while p[n] != n:
        n = p[n]
    return n


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    know = [list(map(int, input().split())) for x in range(M)]
    p = [x for x in range(N + 1)]

    for i in know:
        n1 = i[0]
        n2 = i[1]
        if rep(n1) != rep(n2):
            p[rep(n2)] = rep(n1)
    cnt = 0
    for i in range(1, N + 1):
        if p[i] == i:
            cnt += 1
    print('#{} {}'.format(tc, cnt))