'''
swea 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 D3
'''
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Mat_Weight = list(map(int, input().split()))
    Truck_Weight = list(map(int, input().split()))
    visited = [0] * M

    ans = 0
    for i in range(M):
        result = 0
        for unit_Weight in Mat_Weight:
            if Truck_Weight[i] >= unit_Weight and unit_Weight >= result:
                result = unit_Weight
        if result != 0:
            Mat_Weight.remove(result)
        ans += result
    print('#{} {}'.format(tc, ans))