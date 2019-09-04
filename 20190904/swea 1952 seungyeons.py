t = int(input())
for tc in range(1, t + 1):
    day, month, quarter, year = map(int, input().split())
    plan = list(map(int, input().split()))
    whichone = plan[:]  # 달마다 나가는 돈목록
    # 날이 좋은지 월이 좋은지 확인
    for i in range(12):
        if plan[i] * day < month:
            whichone[i] = plan[i] * day
        else:
            whichone[i] = month
    base = sum(whichone)
    minV = base

    for k in range(5):
        temp = []
        for i in range(10):
            if whichone[i] + whichone[i + 1] + whichone[i + 2] > quarter:
                temp.append([whichone[i] + whichone[i + 1] + whichone[i + 2], i])
        if temp:
            best = temp[0][0]
            idx = temp[0][1]
            for what in range(len(temp)):
                if temp[what][0] > best:
                    best = temp[what][0]
                    idx = temp[what][1]

            minV = minV - (whichone[idx] + whichone[idx + 1] + whichone[idx + 2]) + quarter
            for j in range(3):
                whichone[idx:idx + 3] = [0, 0, 0]
        else:
            break
    if minV > year:
        minV = year
    if minV > 4 * quarter:
        minV = 4 * quarter
    print("#{} {}".format(tc, minV))