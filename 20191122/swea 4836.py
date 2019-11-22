'''
swea 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기 D2
'''

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    red_1st = []
    blue_1st = []
    for i in range(N):
        y1, x1, y2, x2, color = map(int, input().split())
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if color == 1:
                    red_1st.append((y, x))
                elif color == 2:
                    blue_1st.append((y, x))

    result = []
    if len(red_1st) > len(blue_1st):
        for i in blue_1st:
            if i in red_1st:
                result.append(i)

    if len(red_1st) < len(blue_1st):
        for i in red_1st:
            if i in blue_1st:
                result.append(i)

    print('#{} {}'.format(tc, len(result)))