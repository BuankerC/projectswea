for k in range(int(input())):
    n = int(input())
    a = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            g = min(i, j, n-1-i, n-1-j)
            x = 1 + 4 * g * (n-g)
            y = i + j - 2 * g
            if i > j:
                a[i][j] = 4 * (n-1-2*g) - y + x
            else:
                a[i][j] = y + x
    print(f'#{k+1}')
    for i in a:
        print(*i)