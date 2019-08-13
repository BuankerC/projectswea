def GetMax(i):
    max_floor = floor[i-2]
    if max_floor < floor[i-1]:
        max_floor = floor[i-1]
    if max_floor < floor[i+1]:
        max_floor = floor[i+1]
    if max_floor < floor[i+2]:
        max_floor = floor[i+2]

    return max_floor

TC = 10
for tc in range(1, TC+1):
    N = int(input())
    floor = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        side = GetMax(i)
        if side < floor[i]:
            result += floor[i] - side

    print(f'#{tc} {result}')