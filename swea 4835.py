TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))

    lst = []
    for i in range(N-M+1):
        lst.append(sum(Data[i:i+M]))

    print('#%s %d'%(tc, max(lst)-min(lst)))