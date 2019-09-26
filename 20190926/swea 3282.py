'''
swea 3282 .
0/1 Knapsack D3
'''
T = int(input())
for tc in range(1, T + 1):
    line = list(map(int, input().split()))
    n = line[0]  # 부피
    k = line[1]  # 가중치

    items = []
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n):
        items.append(list(map(int, input().split())))

    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            if j >= items[i - 1][0]:  # j는 부피 해당 부피보다 같거나 작은 경우 즉, 해당 부피의 가방에 들어갈 수 있는 경우
                # 해당 1, j 위치에서 dp에서 이전 줄에서 해당 물건의 부피만큼 뺀 값에 현재 물건의 가중치를 더한 것과 바로 위의 가중치 중 큰 것을 넣음
                dp[i][j] = max(dp[i - 1][j - items[i - 1][0]] + items[i - 1][1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print('#' + str(tc), dp[-1][-1])