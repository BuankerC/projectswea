tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    locs = list(map(int, input().split()))
    minl, cnt = 100000, 0
    for l in locs:
        if abs(1) < minl:
            min1 = abs(1)
            cnt = 1
        elif abs(1) == minl:
            cnt += 1
    print('#{} {} {}'.format(t, minl, cnt))
