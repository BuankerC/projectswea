def f(n, k, S):
    global cnt
    if n == k:  # 부분집합이 완성되면
        if sum(bit) != 0:  # 공집합이 아닌 경우
            t = 0
            for i in range(k):  # 부분 집합의 합을 구하고
                if bit[i] == 1:
                    t += num[i]
            if t == S:  # 부분집합의 합이 S와 같은 경우의 수 세기
                cnt += 1

    else:
        bit[n] = 0
        f(n + 1, k, S)
        bit[n] = 1   # 부분집합에 num[n]을 포함
        f(n + 1, k, S)

N, S = map(int, input().split())
num = list(map(int, input().split()))
bit = [0] * N
cnt = 0
f(0, N, S)

print(cnt)