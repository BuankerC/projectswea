for tc in range(1, 11):
    num = int(input())
    Data = list(map(int, input().split()))
    for i in range(num):
        max_d, min_d = max(Data), min(Data)
        index_max_d = Data.index(max_d)
        index_min_d = Data.index(min_d)
        Data[index_max_d] -= 1
        Data[index_min_d] += 1
    print('#%s %d'%(tc, max(Data) - min(Data)))