'''
swea 4371 항구에 들어오는 배 D3
'''

T = int(input())
for tc in range(T):
    N = int(input())
    data = [int(input()) for _ in range(N)]
    count = 0

    for i in range(1, N):
        if data[i] < 0:
            continue
        ans1 = data[i] - 1
        for j in range(i + 1, N):
            if data[j] < 0:
                continue
            ans2 = data[j] - 1
            if ans2 // ans1 == ans2 / ans1:
                data[j] = -1
    for i in range(1, N):
        if data[i] > 0:
            count += 1
    print('#{} {}'.format(tc + 1, count))