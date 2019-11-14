'''
swea 당근 수확 3 D2
'''
for t in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    minV = float('INF')
    for i in range(N-1):
        for j in range(M - 1):
            a, b, c = 0, 0, 0
            for x in range(i + 1):
                a += sum(arr[x][:j + 1])
                b += sum(arr[x][j + 1:])
            for y in range(N - i - 1):
                c += sum(arr[-y - 1])
            minV = min(minV, (abs(a - b) + abs(b - c) + abs(c - a)) // 2)
    print('#{} {}'.format(t + 1, minV))