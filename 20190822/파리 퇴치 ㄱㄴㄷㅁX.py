for T in range(int(input())):
    N, M = map(int, input().split())
    flys = [list(map(int, input().split())) for i in range(N)]

    print(f'#{T+1}', end=' ')
    # ㄱ
    res1 = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            t = sum(flys[i][j:j+M])
            for k in range(i+1, i+M):
                t += flys[k][j+M-1]
            res1 = max(res1, t)
    print(f'ㄱ style result : {res1}', end=', ')

    # ㄴ
    res2 = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            t = sum(flys[i+M-1][j:j+M])
            for k in range(i, i+M-1):
                t += flys[k][j]
            res2 = max(res2, t)
    print(f'ㄴ style result : {res2}', end=', ')

    # ㄷ
    res3 = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            t = sum(flys[i][j:j+M]) + sum(flys[i+M-1][j:j+M])
            for k in range(i+1, i+M-1):
                t += flys[k][j]
            res3 = max(res3, t)
    print(f'ㄷ style result : {res3}', end=', ')

    # ㅁ
    res4 = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            t = sum(flys[i][j:j+M]) + sum(flys[i+M-1][j:j+M])
            for k in range(i+1, i+M-1):
                t += flys[k][j] + flys[k][j+M-1]
            res4 = max(res4, t)
    print(f'ㅁ style result : {res4}', end=', ')

    # X
    res5 = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            t = 0
            for k in range(M):
                t += flys[i+k][j+k] + flys[i+k][j+M-1-k]
            if M % 2:
                t -= flys[i+M//2][j+M//2]
            res5 = max(res5, t)
    print(f'X style result : {res5}', end=', ')

    # check
    res6 = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            t = 0
            for k in range(i, i+M):
                for l in range(j, j+M):
                    if not (j+l) % 2 and (i+k) % 2:
                        t += flys[k][l]
                    elif (j+l) % 2 and not (i+k) % 2:
                        t += flys[k][l]
            res6 = max(res6, t)
    print(f'check style result : {res6}')