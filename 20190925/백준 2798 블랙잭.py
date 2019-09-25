n, m = map(int, input().split())
a = list(map(int, input().split()))
b = len(a)
total = 0
for i in range(0, b - 2):
    for j in range(i + 1, b - 1):
        for k in range(j + 1, b):
            if a[i] + a[j] + a[k] > m:
                continue
            else:
                total = max(total, a[i] + a[j] + a[k])
print(total)