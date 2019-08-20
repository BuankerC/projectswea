testCase = int(input())

for testNum in range(1, testCase + 1):
    a = list(map(int, input().split()))
    N, M = a[0], a[1]
    mos = ''
    for i in range(N):
        mos += input()
        mos += ' '

    b = list(map(int, mos.split()))

    c = 0
    max = 0
    for i in range((N - M + 1)):
        for j in range((N - M + 1)):
            for k in range(M):
                c += sum(b[N * i + j + k * N: N * i + j + M + k * N])
            if max < c:
                max = c
            c = 0

    print('#{0} {1}'.format(testNum, max))