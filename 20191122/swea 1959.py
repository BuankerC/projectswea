'''
swea 1959. 두 개의 숫자열 D2
'''

def f(X, Y):
    maxV = 0
    for i in range(0, len(X) - len(Y) + 1):
        s = 0
        for j in range(0, len(Y)):
            s += X[i + j] * Y[j]
        if maxV < s:
            maxV = s
    return maxV
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        r = f(A, B)
    else:
        r = f(B, A)
    print('#{} {}'.format(tc, r))