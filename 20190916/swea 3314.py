'''
swea 3314. 보충학습과 평균 D3
'''

tc = int(input())
for t in range(1, tc + 1):
    line = list(map(int, input().split()))
    l = len(line)
    ori_avg = sum(line) // l
    under_sum = 0
    for i in line:
        if i < 40:
            under_sum += (40 - i)

    print("#%s %d" % (t, ori_avg + (under_sum // l)))