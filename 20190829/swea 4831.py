T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    stop = [0] * (N + 1)

    for i in charger:
        stop[i] = 1
    last = 0
    cnt = 0
    next_stop = last + K
    while(last + K < N):
        if stop[next_stop] == 0:
            next_stop -= 1
            if next_stop == last:
                break
        else:
            last = next_stop
            next_stop = last + K
            cnt += 1

    if next_stop == last:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, cnt))