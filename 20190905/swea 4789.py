'''
swea 4789 성공적인 공연기획 D3
'''

T = int(input())
for tc in range(T):
    data = list(map(int, input()))
    count, sum = 0, 0
    for i in range(len(data)):
        if sum >= i:
            sum += data[i]
        else:
            count += i - sum
            sum = i + data[i]
    print('#{} {}'.format(tc+1, count))