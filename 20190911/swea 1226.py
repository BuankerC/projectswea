'''
swea 1226 [S/W 문제해결 기본] 7일차 - 미로1 D4
'''

import queue
q = queue.Queue()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def bfs(m, vi):
    global q
    global dx, dy

    find_flag = False
    while not q.empty():
        dot = q.get()
        for i in range(len(dx)):
            nx = dot.x + dx[i]
            ny = dot.y + dy[i]

            if nx < 0 and ny < 0 and nx >= len(m) and ny >= len(m):
                continue

            if (not vi[nx][ny]) and m[nx][ny] == 0 or m[nx][ny] == 3:
                if m[nx][ny] == 3:
                    return 1
                else:
                    q.put(Dot(nx, ny))
                    vi[nx][ny] = True

    if not find_flag:
        return 0

def main():
    global q

    for t in range(1, 11):
        q = queue.Queue()
        n = int(input())
        m = [[0] * 16 for _ in range(16)]
        vi = [[False] * 16 for _ in range(16)]

        start_x = 0
        start_y = 0
        for i in range(16):
            line = input()
            for j in range(16):
                if line[j] == '1':
                    vi[i][j] = True
                elif line[j] == '2':
                    start_x = i
                    start_y = j
                m[i][j] = int(line[j])

        q.put(Dot(start_x, start_y))
        vi[start_x][start_y] = True
        print('#{} {}'.format(n, bfs(m, vi)))

if __name__ == '__main__':
    main()