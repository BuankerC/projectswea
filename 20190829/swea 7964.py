for t in range(int(input())):
    number_castles, limit_distance = map(int, input().split())
    status = ''.join(input().split())
    ans = 0
    distances = list(map(len, status.split('1')))
    for distance in distances:
        ans += distance // limit_distance
    print('#{} {}'.format(t + 1, ans))