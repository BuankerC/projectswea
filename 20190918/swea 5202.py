'''
swea 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 D3
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Data = []
    for i in range(N):
        x, y = map(int, input().split())
        Data.append([x, y])

    # 정렬
    for i in range(N):
        for j in range(i, N):
            if Data[i][1] > Data[j][1]:
                Data[i], Data[j] = Data[j], Data[i]

    result = []
    visited = [0] * N
    result.append(Data[0])
    visited[0] = 1

    while True:
        #제거
        for i in range(N):
            if result[-1][1] > Data[i][0]:
                visited[i] = 1

        if not 0 in visited:
            break

        index = 0
        value = 987654321
        for i in range(N):
            if visited[i] == 0 and result[-1][-1] <= Data[i][0] and Data[i][1] < value:
                index = i
                value = Data[i][0]

        result.append(Data[index])
    print('#{} {}'.format(tc, len(result)))