tc = int(input())
for t in range(1, tc+1):
    nums = list(map(int, input().split()))
    maxn, minn = nums[0], nums[0]
    for i in range(1, 10):
        if nums[i] > maxn:
            maxn = nums[i]
        if nums[i] < minn:
            minn = nums[i]
    total = 0
    for i in nums:
        if n != maxn and n != minn:
            total += n
    print('#%d %d' % (t, round(total/8)))