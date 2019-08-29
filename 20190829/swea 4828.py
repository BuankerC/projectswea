def get_max(num):
    my_max = num[0]
    for i in range(1, len(num)):
        if my_max < num[i]:
            my_max = num[i]
    return my_max

def get_min(num):
    my_min = num[0]
    for i in range(1, len(num)):
        if my_min > num[i]:
            my_min = num[i]
    return my_min

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    num = list(map(int, input().split()))
    result = get_max(num) - get_min(num)
    print('#{} {}'.format(tc, result))