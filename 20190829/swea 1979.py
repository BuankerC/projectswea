tc = int(input())
for t in range(1, tc + 1):
    N, K = map(int, input().split())
    puzz = [[] * N for _ in range(N)]
    for i in range(N):
        puzz[i] = [int(n) for n in input().split()]
    ans = 0
    for i in range(N):
        rowcnt = colcnt = 0
        for j in range(N):
            if puzz[i][j] == 1:
                rowcnt += 1
            elif puzz[i][j] == 0:
                if rowcnt == K:
                    ans += 1
                rowcnt = 0
            if puzz[j][i] == 1:
                colcnt += 1
            elif puzz[j][i] == 0:
                if colcnt == K:
                    ans += 1
                colcnt = 0
        if rowcnt == K:
            ans += 1
        if colcnt == K:
            ans += 1
    print('#{} {}'.format(t, ans))