N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

minS = 100000
for i in range(N):
    for j in range(N):
        s = 0
        for k in range(N):
            s += arr[i][k]
            s += arr[k][j]
        s -= arr[i][j]
        if minS > s:
            minS = s
print(minS)