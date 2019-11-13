'''
swea 2117. [모의 SW 역량테스트] 홈 방범 서비스
'''

cost_k = [0, 1, 5, 13, 25, 41, 61, 85, 113, 145, 181, 221, 265, 313, 365, 421, 481, 545, 613, 685, 761, 841, 925, 1013, 1105]

def count(i, j, K, lim):
    global Max, flag
    cnt = sum(arr[i][max(j- (K - 1), 0): min(j + (K - 1), N - 1) + 1])
    for a in range(1, K):
        r_top, r_bot = i - a, i + a
        if r_top >= 0:
            cnt += sum(arr[r_top][max(j - (K - a - 1), 0): min(j + (K - a - 1), N - 1) + 1])
        if r_bot <= N - 1:
            cnt += sum(arr[r_bot][max(j - (K - a - 1), 0): min(j + (K - a - 1), N - 1) + 1])
    if cnt >= lim:
        if cnt > Max:
            Max = cnt

for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    tot = 0
    arr = [0] * N
    for i in range(N):
        arr[i] = list(map(int, input().split()))
        tot += sum(arr[i])

    total = tot * M
    for e in range(25):
        if cost_k[e] > total:
            break

    Max = 1
    flag = 0
    for K in range(e - 1, 1, -1):
        lim, r = divmod(cost_k[K], M)
        if r:
            lim += 1
        for i in range(N):
            for j in range(N):
                count(i, j, K, lim)
        if flag:
            break

    print(f"#{T} {Max}")