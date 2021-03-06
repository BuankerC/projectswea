def IsSafe(y, x):
    return 0 <= y < N and 0 <= x < N and (Maze[y][x] == 0 or Maze[y][x] == 3)

def DFS(start_y, start_x):
    global result

    if Maze[start_y][start_x] == 3:
        result = 1
        return

    visited.append((start_y, start_x))
    for dir in range(4):
        New_Y = start_y + dy[dir]
        New_X = start_x + dx[dir]
        if IsSafe(New_Y, New_X) and (New_Y, New_X) not in visited:
            DFS(New_Y, New_X)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Maze = [list(map(int, input())) for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if Maze[y][x] == 2:
                start_y, start_x = y, x
    #상, 하, 좌, 우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    visited = []
    result = 0
    DFS(start_y, start_x)
    print('#%d %d'%(tc, result))