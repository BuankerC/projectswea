T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    ans = a + b
    print('Case #{}: {} + {} = {}'.format(tc+1, a, b, a + b))