for test in range(10):
    testcase = input()
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
        cntl += res[99 - i][i]
    ressum.append(cntr)
    ressum.append(cntl)

    print('#{} {}'.format(testcase, max(ressum)))