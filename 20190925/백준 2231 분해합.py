N = int(input())
ans = 0
for i in range(1, N + 1):
    N_list = list(map(int, str(i)))
    ans = i + sum(N_list)

    if ans == N:
        print(i)
        break

    if i == N:
        print(0)