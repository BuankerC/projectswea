T = int(input())
for tc in range(T):
    total = [0]*5000
    for N in range(int(input())):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi+1):
            total[i-1] += 1
    res = []
    for P in range(int(input())):
        Cj = int(input())
        res.append(str(total[Cj-1]))
    print(f'#{tc+1} {" ".join(res)}')