TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))
    for i in range(M):
        Data.append(Data.pop(0))
    print(f'#{tc} {Data[0]}')