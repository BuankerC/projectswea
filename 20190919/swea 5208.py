'''
swea 5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2 D3
'''

def DFS(num):
    global cnt, result

    if num >= N:
        if result > cnt:
            result = cnt
        return

    if result < cnt:
        return

    start = num
    life = Data[start]

    for i in range(start + life, start, -1):
        cnt += 1
        DFS(i)
        cnt -= 1

T = int(input())
for tc in range(1, T + 1):
    Data = list(map(int, input().split()))
    N = Data[0]
    result = 987654321
    cnt = 0

    DFS(1)

    print('#{} {}'.format(tc, result - 1))