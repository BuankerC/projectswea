'''
swea 1861. 정사각형 방 D4
'''
big = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(m, x, y, n):
    cnt = 1
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and (m[x][y] + 1 == m[nx][ny]):
            cnt += dfs(m, nx, ny, n)

    return cnt

def main():
    global big

    tc = int(input())
    for t in range(1, tc + 1):
        n = int(input())
        m = [[0] * n for _ in range(n)]

        for i in range(n):
            line = list(map(int, input().split()))
            for j in range(n):
                m[i][j] = line[j]

        big = 0
        room_no = 999999999
        for i in range(n):
            for j in range(n):
                cnt = dfs(m, i, j, n)
                if big <= cnt:
                    if big == cnt and room_no > m[i][j]:
                        room_no = m[i][j]
                    elif big != cnt:
                        room_no = m[i][j]
                    big = cnt

        print('#{} {} {}'.format(t, room_no, big))

if __name__ == '__main__':
    main()