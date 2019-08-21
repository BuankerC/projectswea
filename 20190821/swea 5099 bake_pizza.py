TC = int(input())

for tc in range(1, TC+1):
    N,M = map(int, input().split())
    Data = list(map(int, input().split()))
    Q = []
    for i in range(N):
        Q.append([Data[i], i])
    # print(Q)

    i = 0
    while len(Q)!=1:
        Q[0][0] //= 2

        if Q[0][0] == 0:
            if N+ i < M:
                Q.pop(0)
                Q.append([Data[N+i], N+i])
                i+=1
            elif N+i >= M:
                Q.pop(0)
        else:
            Q.append(Q.pop(0))

    print(f'#{tc} {Q[0][1]+1}')
