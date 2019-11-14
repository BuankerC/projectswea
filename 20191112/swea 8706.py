'''
swea 8706 당근 수확 2
'''
T = int(input()) + 1
for tc in range(1, T):
    N, M = map(int, input().split())
    carrot = list(map(int, input().split()))
    road = 0
    i = 0
    wag = 0
    while(i < N):
        wag += carrot[i]
        while wag >= M:
            road += (i + 1) * 2
            wag -= M
        road += 1
        i += 1
    print(f'#{tc} {road + i}')