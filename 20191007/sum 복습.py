'''
swea 1209. [S/W 문제해결 기본] 2일차 - Sum
'''

for test in range(10):
    tc = input()
    res = []
    ressum = []

    for i in range(100):
        numbers = list(map(int, input().split()))
        res.append(numbers)

    column = list(zip(*res))

    cntr, cntl = 0, 0

    for i in range(100):
        ressum.append(sum(res[i]))
        ressum.append(sum(column[i]))
        cntr += res[i][i]
        cntl += res[99-1][i]
    ressum.append(cntr)
    ressum.append(cntl)
    print('#{} {}'.format(tc. max(ressum)))
