for t in range(1, int(input()) + 1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))

    dp = [0] * 13
    for i in range(1, 13):
        dp[i] = min(dp[i - 1] + plan[i - 1] * price[0], dp[i - 1] + price[1])
        if i >= 3:
            dp[i] = min(dp[i - 3] + price[2], dp[i])

    res = min(dp[12], price[3])

    print("#%d %d" % (t, res))