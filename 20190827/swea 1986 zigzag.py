T = int(input())
for t in range(T):
    N = int(input())
    result = 0
    for n in range(1, N + 1):
        if n % 2:
            result += n
        else:
            result -= n
    print('#{} {}'.format(t+1, result))