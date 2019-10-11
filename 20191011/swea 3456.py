'''
swea 3456. 직사각형 길이 찾기 D3
'''

T = int(input())
for tc in range(1, T + 1):
    d = {}
    line = list(map(int, input().split()))
    for i in line:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    print("#%d " %(tc), end='')
    for i in d:
        if d[i] % 2 == 1:
            print(i, end='')
    print()