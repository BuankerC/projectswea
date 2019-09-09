def f(i, N):
    if i > N:
        for i in range(1, i):
            if L[i] == 1:
                print(i, end =' ')
            print()
    else:
        L[i] = 0
        f(i+1, N)
        L[i] = 1
        f(i+1, N)

N = 5
L = [0]*(N+1)
f(1, N)
