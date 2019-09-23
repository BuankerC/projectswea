'''
1244. [S/W 문제해결 응용] 2일차 - 최대 상금 D3
'''

def swap(a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return

def made(a):
    res = 0
    rev = arr[::-1]
    for i in range(L):
        res += rev[i] * 10 ** i
    return res

def solve(s):
    global calling
    if s == b:
        if made(arr) > calling:
            calling = made(arr)
        return
    for i in range(L):
        for j in range(L):
            if i < j:
                swap(i, j)
                solve(s + 1)
                swap(i, j)
T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    if b > 2:
        b = b // 2 + 1
    arr = list(map(int, list(str(a))))
    L = len(arr)
    calling = 0
    used = [0] * L
    solve(0)
    print('#{} {}'.format(tc + 1, calling))