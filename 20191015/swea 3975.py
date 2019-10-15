'''
swea 3975. 승률 비교하기 D3
'''

arr = ['ALICE', 'BOB', 'DRAW']
T = int(input())
code = []
for tc in range(T):
    a, b, c, d = map(int, input().split())
    f = (a / b) - (c / d)
    if f > 0:
        code.append(0)
    elif f < 0:
        code.append(1)
    else:
        code.append(2)
for i in range(T):
    print('#{} {}'.format(i + 1, arr[code[i]]))