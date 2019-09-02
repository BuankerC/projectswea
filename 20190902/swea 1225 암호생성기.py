for T in range(10):
    tn = int(input())
    nlst = list(map(int, input().split()))
    while nlst[-1] != 0:
        for i in range(5):
            temp = nlst[0] - (i+1)
            nlst[0:7] = nlst[1:]
            nlst[-1] = temp
            if nlst[-1] <= 0:
                nlst[-1] = 0
                break
    nlst = list(map(str, nlst))
    res = ' '.join(nlst)
    print(f'#{tn} {res}')