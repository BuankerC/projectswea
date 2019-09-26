'''
100 X 100 2차원 배열을 같은 높이로 만든다. 높이의 범위는 1 ~ 29이다.
이 때 각 칸의 비용이 정해지면 이 비용으로 SUM 문제를 풀어본다.
SUM의 최소 값 구하기, 이 때의 높이 (최소 값이 같다면 더 낮은 높이)
'''
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
    for i in range(100):
        sero = 0
        for j in range(100):
            sero += grid[j][i]
        minVal2 = min(sero, minVal2)

    for i in range(100):
        result1 += grid[i][i]
    for i in range(100):
        result2 += grid[i][99 - i]

    minVal2 = min(result1, minVal2, result2)
    print('#{} {} {}'.format(case, targetheight, minVal2))