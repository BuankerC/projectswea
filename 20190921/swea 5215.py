'''
swea 5215 햄버거 다이어트 D3
'''
tc = int(input())
for i in range(0, tc):
    tmp = input().split(' ')
    burger_num = int(tmp[0])
    max_cal = int(tmp[1])
    max_val = 0
    scores = []
    cals = []
    for j in range(0, burger_num):
        tmp = input().split(' ')
        scores.append(int(tmp[0]))
        cals.append(int(tmp[1]))

    for j in range(0, (1<<burger_num)):
        sum_score = 0
        sum_cal = 0
        for k in range(0, burger_num):
            if j & (1 << k):
                sum_cal += cals[k]
                sum_score += scores[k]
                if sum_cal > max_cal:
                    sum_score = 0
                    break
        if max_val < sum_score:
            max_val = sum_score
    print('#' + str(i + 1) + ' ' + str(max_val))