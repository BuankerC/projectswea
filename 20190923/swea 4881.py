'''
swea 4881. [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합 D2
'''

def Calc(y):
    global sub_result, result

    if result < sub_result:
        return

    if y == N:
        if sub_result < result:
            result = sub_result
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            sub_result += lst[y][x]
            Calc(y + 1)
            visited[x] = False
            sub_result -= lst[y][x]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_result, result = 0, 987654321
    Calc(0)

    print('#{} {}'.format(tc, result))