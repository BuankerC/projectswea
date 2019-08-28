T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    maxV = -1
    for i in range(N-1):
        for j in range(i+1, N):
            m = A[i]*A[j]
            if m > 10 and m > maxV:
                n = m
                t = 10
                while(n > 0 and n % 10 <= t):
                    t = n % 10
                    n = n // 10
                if n == 0:
                    maxV = m
    print('#{} {}'.format(tc, maxV))