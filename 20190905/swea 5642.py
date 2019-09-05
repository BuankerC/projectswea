'''
swea 5642 [Professional] 합
'''
for t in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))
    temp_sum = num[0]
    result = num[0]
    for idx in range(1, len(num)):
        temp_sum = max(temp_sum + num[idx], num[idx])
        result = max(temp_sum, result)
    print('#{} {}'.format(t+1, result))