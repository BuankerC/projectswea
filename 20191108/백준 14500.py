N, M = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]\

di = [[0, 0, 0], [1, 2, 3], [0, 1, 1], [1, 2, 2], [0, 0, -1], [-1, -2, -2], [0, 0, 1], [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 0, -1], [1, 1, 2], [0, -1, -1], [1, 1, 2], [0, 1, 1], [0, 0, 1], [-1, -1, -2], [0, 0, -1], [1, 1, 2]]
dj = [[1, 2, 3], [0, 0, 0], [1, 0, 1], [0, 0, 1], [1, 2, 2], [0, 0, -1], [-1, -2, -2], [0, 0, -1], [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 1, 1], [1, 1, 2], [0, -1, -1], [1, 1, 2], [1, 2, 1], [0, 1, 0], [-1, -2, -1], [-1, 0, 0]]

max_sum = 0

for i in range(N):
    for j in range(M):
        for a in range(19):
            block_sum = area[i][j]
            for b in range(3):
                x = i + di[a][b]
                y = j + dj[a][b]
                if 0 <= x <= N - 1 and 0 <= y <= M - 1:
                    block_sum += area[x][y]
                else:
                    break
            else:
                if block_sum > max_sum:
                    max_sum = block_sum
print(max_sum)