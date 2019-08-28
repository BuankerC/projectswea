T = int(input())
N = int(input())
cnt = 0
for i in range(1, N):
    s = 0
    for j in range(i, N):
        s += j
        if s == N:
            cnt += 1
            break
        elif s > N:
            break
print(cnt)