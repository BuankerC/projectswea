for T in range(int(input())):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))

    idx = 0
    for i in range(K):
        idx += M
        if idx > len(nums):
            idx %= len(nums)
        nums.insert(idx, nums[idx-1] + nums[idx%len(nums)])
    print('#{} {}'.format(T+1, ' '.join(map(str, nums[::-1][:10]))))