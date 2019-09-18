'''
swea 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 D3
'''
N = 3
M = 2
weight = [1, 5, 3]
truck = [8, 3]

weight.sort()  # 오름차순 정렬
truck.sort()

idxW = N - 1  # 가장 무거운 화물
idxT = M - 1  # 가장 큰 트럭
total = 0
while(idxT >= 0 and idxW >= 0):  # 트럭과 화물이 남아있는 동안
    if weight[idxW] <= truck[idxT]:  # 현재 가장 무거운 화물을 현재 가장 큰 트럭에 옮길 수 있으면
        total += weight[idxW]
        idxW -= 1
        idxT -= 1
    else:  # 옮길 수 없으면 해당 컨테이너는 포기하고 다음 컨테이너 선택
        idxW -= 1
print(total)
