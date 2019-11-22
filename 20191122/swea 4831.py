'''
swea 4831. [파이썬 S/W 문제해결 기본] 1일차 - 전기버스 D3
'''

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))
    stop = [0] * (N + 1) # 충전기 위치 표시
    for i in charger:
        stop[i] = 1
    last = 0
    cnt = 0
    next_stop = last + K  # 최대로 이동 가능한 정류장
    while(last + K < N):  # 종점에 도착하기 전이면
        if stop[next_stop] == 0:  # 다음 최대 이동 거리에 충전기가 없으면
            next_stop -= 1
            if next_stop == last:  # 마직막 충전 위치까지 되돌아오면
                break  # 운행중단
        else:  # 마지막 충전 위치 이후에 충전기가 있으면
            last = next_stop  # 충전기를 마지막 충전 위치로 기록
            next_stop = last + K  # 현재 위치에서 최대 이동 가능 거리 계산
            cnt += 1  # 춛전 횟수 1 증가

    if next_stop == last:  # 운행 중단인 경우
        print('#{} 0'.format(tc))
    else:  # 종점에 도착한 경우
        print('#{} {}'.format(tc, cnt))