T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stop = [0] + list(map(int, input().split())) + [N]
    last = 0  # 마지막 충전기 인덱스
    cnt = 0
    result = 1
    for i in range(1, M+2):
        if stop[i] - stop[i-1] > K:  # 두 충전기 거리가 K보다 크면 중단
            result = 0
            break
        else:
            if stop[i] - stop[last] > K:  # i번 충전기에 도착할 수 없으면
                last = i - 1  # 하나 전 충전기에서 충전하고
                cnt += 1  # 충전횟수 증가
    if result == 0:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, cnt))