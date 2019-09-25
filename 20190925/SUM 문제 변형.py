'''
100 X 100 2차원 배열을 같은 높이로 만든다. 높이의 범위는 1 ~ 29이다.
이 때 각 칸의 비용이 정해지면 이 비용으로 SUM 문제를 풀어본다.
SUM의 최소 값 구하기, 이 때의 높이 (최소 값이 같다면 더 낮은 높이)
'''
# minS = 100000000
# arr = []
# for h in range(1, 30):
#     for i in range(100):
#         minV = 100000000
#         right = arr[i][i]
#         left = arr[i][99-i]
#         for j in range(100):
#             row += arr[i][j]
#             col += arr[j][i]
#         minV = right, left, row, col
#     if minS > minV

# for tc in range(10):
#     tc = input()
#     res = []
#     ressum = []
#
#     for i in range(100):
#         numbers = list(map(int, input().split()))
#         res.append(numbers)
#
#     column = list(zip(*res))
#
#     cntr, cntl = 0, 0
#
#     for i in range(100):
#         ressum.append(sum(res[i]))
#         ressum.append(sum(column[i]))
#         cntr += res[i][i]
#         cntl += res[99 - i][i]
#     ressum.append(cntr)
#     ressum.append(cntl)
#     print('#{} {}'.format(tc, min(ressum)))

for h in range(1, 29):
    arr = 0
    for i in range(100):
        numbers = list(map(int, input().split()))
        res.