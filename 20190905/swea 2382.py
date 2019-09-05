'''
swea 2382 미생물 격리
'''
def sum_microbe():
    check = [False for _ in range(len(data))]
    temp = []
    for i in range(len(data)):
        if check[i]:
            continue
        check[i] = True
        t = [i]
        for j in range(i+1, len(data)):
            if data[i][0] == data[j][0] and data[i][1] == data[j][1] and not check[j]:
                t.append(j)
                check[j] = True
        temp.append(t)
    result = []
    for t in temp:
        big = data[t[0]]
        cnt = 0
        for i in t:
            cnt += data[i][2]
            if big[2] < data[i][2]:
                big = data[i]
        big[2] = cnt
        result.append(big)
    return result

dxy = [0, [-1, 0], [1, 0], [0, -1], [0, 1]]
for T in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    data = []
    for _ in range(K):
        data.append(list(map(int, input().split())))
    for _ in range(M):
        for microbe in data:
            microbe[0] += dxy[microbe[3]][0]
            microbe[1] += dxy[microbe[3]][1]
        data = sum_microbe()
        for microbe in data:
            if microbe[0] in [0, N - 1] or microbe[1] in [0, N - 1]:
                microbe[2] //= 2
                if microbe[3] == 1:
                    microbe[3] = 2
                elif microbe[3] == 2:
                    microbe[3] = 1
                elif microbe[3] == 3:
                    microbe[3] = 4
                elif microbe[3] == 4:
                    microbe[3] = 3
    result = 0
    for microbe in data:
        result += microbe[2]
    print('#{} {}'.format(T, result))