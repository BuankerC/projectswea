import sys
sys.stdin = open('sum.txt', 'r')

for case in range(1, int(input()) + 1):
    grid = [list(map(int, input().split())) for _ in range(100)]
    minVal = float('inf')
    targetheight = -1
    for height in range(29, 0, -1):
        nohope = 0
        result = 0
        for i in range(100):
            for j in range(100):
                result += abs(height - grid[i][j])
                if result > minVal:
                    nohope = 1
                    break
            if nohope == 1:
                break
        else:
            minVal = result
            targetheight = height

    for i in range(100):
        for j in range(100):
            grid[i][j] = abs(targetheight - grid[i][j])

    minVal2 = float('inf')

    result1 = 0
    result2 = 0
    for i in range(100):
        minVal2 = min(minVal2, sum(grid[i]))
        minVal2 = min(minVal2, sum(list(zip(*grid))[i]))
        result1 += grid[i][i]
        result2 += grid[i][99 - i]

    minVal2 = min(result1, minVal2, result2)
    print('#{} {} {}'.format(case, targetheight, minVal2))