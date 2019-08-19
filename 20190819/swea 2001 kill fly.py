for t in range(int(input())):
    a, b = map(int, input().split())
    count = a-b+1
    result = []
    for i in range(a):
        num = list(map(int, input().split()))
        result.append(num)
    lists = []
    for j in range(count):
        for r in range(count):
            total = 0
            for s in range(0, b):
                total += sum(result[j+s][r:r+b])
            lists.append(total)
    print(f'#{t+1} {max(lists)}')