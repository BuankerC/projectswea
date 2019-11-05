'''
swea 3809. 화섭이의 정수 나열 D3
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = ''
    while len(cards) != N:
        cards += ''.join(input().split())
    cnt = 0
    while str(cnt) in cards:
        cnt += 1
    print('#{} {}'.format(tc, cnt))