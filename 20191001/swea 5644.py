'''
swea 5644. [모의 SW 역량테스트] 무선 충전
'''
def mark(x, y, c, p, cnt):
    if cnt == c:
        return

    for i in range(1, 5):
        tmpx, tmpy = x + dx[i], y + dy[i]
        if 0 <= tmpx < 10 and 0 <= tmpy < 10:
            if not p in m[tmpx][tmpy]:
                m[tmpx][tmpy].append(p)
            mark(tmpx, tmpy, c, p, cnt + 1)

dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]
for tc in range(1, int(input()) + 1):
    M, A = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    m = [[[], [], [], [], [], [], [], [], [], []] for _ in range(10)]
    for i in range(A):
        y, x, c, p = map(int, input().split())
        m[x - 1][y - 1].append(p)
        mark(x - 1, y - 1, c, p, 0)

    ax, ay = 0, 0
    bx, by = 9, 9
    resulta, resultb = 0, 0
    cnt = [0] * 501
    if len(m[ax][ay]) > 0:
        resulta += max(m[ax][ay])
    if len(m[bx][by]) > 0:
        resultb += max(m[bx][by])
    for t in range(M):
        ax, ay = ax + dx[a[t]], ay + dy[a[t]]
        bx, by = bx + dx[b[t]], by + dy[b[t]]
        max_a, max_b = 0, 0
        if len(m[ax][ay]) > 0:
            for i in m[ax][ay]:
                cnt[i] += 1
        if len(m[bx][by]) > 0:
            for i in m[bx][by]:
                cnt[i] += 1
        if len(m[ax][ay]) > 0:
            max_a = m[ax][ay][0] // cnt[m[ax][ay][0]]
            for i in m[ax][ay]:
                if i // cnt[i] > max_a:
                    max_a = i // cnt[i]
        if len(m[bx][by]) > 0:
            max_b = m[bx][by][0] // cnt[m[bx][by][0]]
            for i in m[bx][by]:
                if i // cnt[i] > max_b:
                    max_b = i // cnt[i]
        resulta += max_a
        resultb += max_b
    result = resulta + resultb
    print("#{} {}".format(tc, result))