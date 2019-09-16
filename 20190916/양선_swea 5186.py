'''
swea 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 D2
'''

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    ans = ''
    c = -1
    while N != 0:
        if c == -13:
            ans = 'overflow'
            break
        if N >= 2 ** c:
            ans += '1'
            N -= 2 ** c
        else:
            ans += '0'
        c -= 1
    print('#{} {}'.format(tc, ans))