for tc in range(int(input())):
    nums = [int(input()) for n in range(int(input()))]
    ave = sum(nums)//len(nums)
    cnt = 0
    for i in range(len(nums)):
        if nums[i] > ave:
            cnt += nums[i] - ave
    print('#{} {}'.format(tc+1, cnt))