T = int(input())
for t in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    result = []
    max_ = 0
    for n in nums[::-1]:
        if max_ < n:
            result.append(max_ - n)
            max_ = n
        elif max_ >= n:
            result.append(max_ - n)
    print(f"#{t} {max(result[1:])}")