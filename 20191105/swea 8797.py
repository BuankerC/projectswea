'''
swea 8797. 당근수확4
'''

for tc in range(1, int(input()) + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    a, b, c, d = 0, 0, 0, 0
    for i in range(n // 2):
        for j in range(i + 1, n - (i + 1)):
            a += arr[i][j]
            b += arr[j][i]
    for i in range(n // 2 + 1, n):
        for j in range(n - i, i):
            c += arr[i][j]
            d += arr[j][i]
    print('#{} {}'.format(tc, max(a, b, c, d) - min(a, b, c, d)))