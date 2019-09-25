def gcd(x, y):
    mod = x % y
    while mod > 0:
        x = y
        y = mod
        mod = x % y
    return y

def lcm(x, y):
    return x * y // gcd(x, y)

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    max_num = lcm(M, N)
    i = 0

    while M * i + x <= max_num:
        if (M * i + x) % N == y or ((M * i + x) % N == 0 and y == N):
            answer = M * i + x
            break
        answer = -1
        i += 1
    print(answer)