Case = input()

tlist = [list(map(int, input().split())) for _ in range(int(case))]

def room(H, W, N):
    Y = H if ((N % H) == 0) else N % H
    X = (N // H) if ((N % H) == 0) else ((N // H) + 1)

    emp = ''

    if (X < 10):
        emp = 0
    return print(str(Y) + emp + str(X))

for H, W, N in tlist:
    room(H, W, N)