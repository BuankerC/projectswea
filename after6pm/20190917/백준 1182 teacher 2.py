def f2(n, k, S, ts, m):  # ts 현재까지 포함시킨 원소의 합, 원소의 개수
    global cnt
    if n == k:
        if m > 0 and ts == S:
            cnt += 1
    else:
        f2(n+1, k, S, ts, m)
        f2(n+1, k, S, ts+num[n], m+1)

N, S = map(int, input().split())
num = list(map(int, input().split()))
bit = [0] * N
cnt = 0
f2(0, N, S, 0, 0)

print(cnt)