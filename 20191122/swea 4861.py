'''
swea 4861. [파이썬 S/W 문제해결 기본] 3일차 - 회문 D2
'''

TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    result = []

    Garo_lst = []
    for i in range(N):
        Data = input()
        Garo_lst.append(Data)
        for i in range(len(Data) - M + 1):
            if Data[i : M + i] == Data[i : M + i][:: -1]:
                result.append(Data[i : M + i])

    Sero_lst = []
    Sero_sub_lst = ''
    for x in range(N):
        for y in Garo_lst:
            Sero_sub_lst += y[x]
        Sero_lst.append(Sero_sub_lst)
        Sero_sub_lst = ''

    for sero_data in Sero_lst:
        for j in range(len(sero_data) - M + 1):
            if sero_data[j : M + j] == sero_data[j : M + j][:: -1]:
                result.append(sero_data[j : M + j])

    print('#{} {}'.format(tc, result[0]))