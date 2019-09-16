'''
swea 3376 파도반 수열 D3
'''

dp = []

def pado():
    global dp

    for i in range(3, 101):
        dp[i] = dp[i-2] + dp[i-3]

def main():
    global dp
    dp = [0] * 101
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    pado()

    tc = int(input())
    for t in range(1, tc + 1):
        n = int(input())
        print('#{} {}'.format(t, dp[n-1]))

if __name__ == '__main__':
    main()