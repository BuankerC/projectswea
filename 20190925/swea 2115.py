'''
swea 2115. [모의 SW 역량테스트] 벌꿀채취
'''

def find(o, now, value, prev, res):
    global res_value, max_value, selected
    if now == M or value > C:
        if value > C:
            if res_value[o] < res - prev ** 2:
                res_value[o] = res - prev ** 2
        else:
            if res_value[o] < res:
                res_value[o] = res

    else:
        for f in range(now, M):
            if not selected[o][f]:
                selected[o][f] = 1
                find(o, f + 1, value + temp[f], temp[f], res + temp[f] ** 2)
                selected[o][f] = 0

for tc in range(1, 1 + int(input())):
    N, M, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_value = set()

    selected = [[0] * M, [0] * M]
    for i in range(N):
        for j in range(N - M + 1):
            if i == N - 1 and N - j - M < M:
                break
            res_value = [0, 0]
            temp = data[i][j:j + M]
            find(0, 0, 0, 0, 0)
            for x in range(i, N):
                if x == i:
                    for y in range(j + M, N - M + 1):
                        temp = data[x][y:y + M]
                        find(1, 0, 0, 0, 0)
                        max_value.add(res_value[0] + res_value[1])
                else:
                    for y in range(N - M + 1):
                        temp = data[x][y:y + M]
                        find(1, 0, 0, 0, 0)
                        max_value.add(res_value[0] + res_value[1])

    print('#{} {}'.format(tc, max(max_value)))