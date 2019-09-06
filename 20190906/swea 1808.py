'''
swea 1808 지희의 고장난 계산기 D4
'''
N = int(1e6)
click = [int(1e9)] * (N + 1)
button = list()

def check(N):
    clicks = 0
    while (N):
        d1 = N % 10
        if not button[d1]:
            return int(1e9)
        clicks += 1
        N //= 10
    return clicks

def solve(N):
    if click[N] < 1e9:
        return click[N]

    click[N] = check(N)
    for div in range(2, int(N ** 0.5)):
        if N % div == 0:
            click[N] = min(click[N], solve(div) + solve(N // div) + 1)
    return click[N]


T = int(input())

for t in range(1, T + 1):
    button = list(map(int, input().split()))
    N = int(input())
    for i in range(N + 1):
        click[i] = int(1e9)

    sol = solve(N) + 1
    if sol > int(1e9):
        sol = -1

    print('#%d %d' % (t, sol))