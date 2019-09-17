'''
swea 5188 [파이썬 S/W 문제해결 구현] 2일차 - 최소합 D3
'''

def Safe(y, x):
    return 0 <= y < N and 0 <= x < N

def DFS(y, x):
    global sub_result, result

    if result < sub_result:
        return

    if y == N - 1 and x == N - 1:
        result = sub_result
        return

    for dir in range(2):
        NewY = y + dy[dir]
        NewX = x + dx[dir]
        if Safe(NewY, NewX) and (NewY, NewX) not in visited:
            visited.append((NewY, NewX))
            sub_result += Data[NewY][NewX]
            DFS(NewY, NewX)
            visited.remove((NewY, NewX))
            sub_result -= Data[NewY][NewX]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]

    visited = []

    # 오른쪽 아래
    dy = [0, 1]
    dx = [1, 0]

    sub_result, result = Data[0][0], 987654321
    DFS(0, 0)
    print('#{} {}'.format(tc, result))