tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    arr = sorted([int(i) for i in input().split()])

    result = [0] * 10
    for i in range(0, 10):
        if i % 2 == 0:
            result[i] = str(arr.pop())
        else:
            result[i] = str(arr.pop(0))
    s = ' '.join(result)
    print(f'#{t} {s}')