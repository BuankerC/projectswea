'''
swea 1986. 지그재그 숫자 D2
'''

T = int(input())
for tc in range(T):
    N = int(input())
    result = 0
    for n in range(1, N + 1):
        if n % 2:
            result += n
        else:
            result -= n
    print('#{} {}'.format(tc + 1, result))