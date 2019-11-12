'''
swea 5643 [Professional] 키 순서 D4
'''

inf = 99999


def main():
    for t in range(1, int(input())+1):
        n = int(input())
        m = int(input())
        map_ = [[inf]*(n+1) for _ in range(n+1)]

        for i in range(m):
            a, b = map(int, input().split())
            map_[a][b] = 1

        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    tmp = map_[i][k] + map_[k][j]
                    if map_[i][j] > tmp:
                        map_[i][j] = tmp

        cnt = 0
        high = [0]*(n+1)
        low = [0]*(n+1)

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    continue

                if map_[i][j] != inf:
                    high[i] += 1
                    low[j] += 1

        for i in range(1, n+1):
            if high[i] + low[i] == n - 1:
                cnt += 1

        print("#%d %d" %(t, cnt))


if __name__ == '__main__':
    main()