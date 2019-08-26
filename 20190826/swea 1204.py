T = int(input())
for tc in range(1, T + 1):
    input()
    scores = list(map(int, input().split()))
    cnt = {}
    for score in scores:
        if score in cnt:
            cnt[score] += 1
        else:
            cnt[score] = 1
    ans = -1
    maxcnt = -1
    for k, v in cnt.items():
        if v > maxcnt:
            maxcnt = v
            ans = k
    print('#{} {}'.format(tc, ans))