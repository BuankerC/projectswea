T = int(input())
for i in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m1 == m2:
        ans = d2 - d1 + 1
    else:
        ans = days[m1] - d1 + d2 + 1
        for m in range(m1+1, m2):
            ans += days[m]
    print('#%d %d' % (i, ans))