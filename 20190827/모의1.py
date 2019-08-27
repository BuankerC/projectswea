T = int(input())
# N = map(int, input().split())
for i in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    purchase_price = -1000

    for j in range(len(prices)):
        if min(prices[:-1]) == prices[j]:
            purchase_price = j
    selling_price = prices[purchase_price+1:]

    maximum_profit = max(selling_price) - prices[j]
    print('#{} {}'.format(i, maximum_profit))