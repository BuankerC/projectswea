for T in range(int(input())):
    L = [list(input()) for _ in range(5)]
    a = max(map(len, L))
    for r in L:
        while len(r) < a:
            r.append('')
    re = ''.join([L[x][y] for y in range(a) for x in range(len(L))])
    print("#{} {}".format(T+1, re))