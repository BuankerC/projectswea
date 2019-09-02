for T in range(int(input())):
    D, A, B = map(int, input().split())
    D = str(D)
    check = [0, 0] + [1] * (B-1)
    for i in range(2, int(B**0.5)+1):
        if check[i]:
            for j in range(2*i, B+1, i):
                check[j] = 0
    tenes = [i for i in range(A, B+1) if check[i] == 1 and D in str(i)]
    print('#{} {}'.format(T+1, len(tenes)))
