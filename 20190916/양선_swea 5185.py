'''
swea 5185 [파이썬 S/W 문제해결 구현] 1일차 - 이진수 D2
'''

T = int(input())
for tc in range(1, T + 1):
    N, hexn = input().split()
    N = int(N)
    binn = ''
    for i in range(N):
        for j in range(3, -1, -1):
            if int(hexn[i], 16) & 1 << j:
                binn += '1'
            else:
                binn += '0'
    print('#{} {}'.format(tc, binn))