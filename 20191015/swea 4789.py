'''
swea 4789. 성공적인 공연 기획 D3
'''

T = int(input())
for tc in range(T):
    data = list(map(int, input()))
    cnt, plus = 0, 0
    for i in range(len(data)):
        if plus >= i:
            plus += data[i]
        else:
            cnt += i - plus
            plus = i + data[i]
    print('#{} {}'.format(tc + 1, cnt))