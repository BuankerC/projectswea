'''
swea 8702. 당근 수확
'''
for T in range(int(input())):
    N = int(input())
    carrots = list(map(int, input().split()))

    area, res = N, sum(carrots)
    for i in range(N - 1):
        p1, p2 = sum(carrots[:i + 1]), sum(carrots[i + 1:])

        diff = p1 - p2 if p1 >= p2 else p2 -p1

        if res > diff:
            res = diff
            area = i + 1
    print(f'#{T + 1} {area} {res}')