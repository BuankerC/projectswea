T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    for m in range(M):
        temp = list(map(int, input().split()))
        for idx, val in enumerate(result):
            if temp[0] < val:
                result = result[:idx] + temp + result[idx:]
                break
        else:
            result.extend(temp)
        if len(result) >= 10+N:
            result = result[-9-N:]
    print(f"#{t} {' '.join(map(str, result[-1:-11:-1]))}")