'''
swea 4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임 D2
'''

T = int(input())

def game(a, b):
    A, B = lst[a - 1], lst[b - 1]
    vs = {1: 3, 2: 1, 3: 2}
    if vs[A] == B:
        return a
    if vs[B] == A:
        return b
    return a

def divide(start, end):
    if start == end:
        return start
    left, right = divide(start, (start + end) // 2), divide((start + end) // 2 + 1, end)
    return game(left, right)

for tc in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print('#{} {}'.format(tc + 1, divide(1, N)))