'''
백준 14502 연구소
'''

import copy
import sys

n = m = 0
arr = []
virusList = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
maxVal = 0

def getSafeArea(copied):
    safe = 0
    for i in range(n):
        for j in range(m):
            if copied[i][j] == 0:
                safe += 1
    return safe

def spreadVirus(x, y, copied):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < m:
            if copied[nx][ny] == 0:
                copied[nx][ny] = 2
                spreadVirus(nx, ny, copied)

def setWall(start, depth):
    global maxVal

    if depth == 3:
        copied = copy.deepcopy(arr)

        length = len(virusList)
        for i in range(length):
            [virusX, virusY] = virusList[i]
            spreadVirus(virusX, virusY, copied)

        maxVal = max(maxVal, getSafeArea(copied))
        return

    for i in range(start, n * m):
        x = (int) (i / m)
        y = (int) (i % m)

        if arr[x][y] == 0:
            arr[x][y] = 1
            setWall(i + 1, depth + 1)
            arr[x][y] = 0

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                 virusList.append([i, j])

    setWall(0, 0)
    print(maxVal)