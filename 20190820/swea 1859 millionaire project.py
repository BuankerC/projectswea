T = int(input())
for tc in range(1, T + 1):
    days = int(input())
    prices = list(map(int, input().split()))

    max_price = prices[-1]
    temp = 0
    gain = 0

    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > max_price:
            max_price = prices[i]
        else:
            gain += (max_price - prices[i])
    print("#{} {}".format(tc, gain))