'''
swea 5656 [모의 SW 역량테스트] 벽돌 깨기
'''

from collections import deque

dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]

def is_in_set(x, y, sets):
    for a, b, c in sets:
        if a == x and b == y:
            return True
    return False

def get_brick_n(x, y, sets):
    for a, b, c in sets:
        if a == x and b == y:
            return c
    return False

def break_brick(w, bricks):
    breaked = set({})
    q.clear()
    h = 0
    while h < H - 1 and not is_in_set(h, w, bricks):
        h += 1
    if not is_in_set(h, w, bricks):
        return breaked
    q.append((h, w, get_brick_n(h, w, bricks)))
    breaked.add((h, w, get_brick_n(h, w, bricks)))
    while len(q):
        x, y, v = q.popleft()
        for d in dxy:
            nx, ny = x, y
            for i in range(v - 1):
                nx += d[0]
                ny += d[1]
                if 0 <= nx < H and 0 <= ny < W and is_in_set(nx, ny, bricks) and not is_in_set(nx, ny, breaked):
                    breaked.add((nx, ny, get_brick_n(nx, ny, bricks)))
                    q.append((nx, ny, get_brick_n(nx, ny, bricks)))
    return breaked

def down(bricks):
    temp = [[] for _ in range(W)]
    for values in bricks:
        temp[values[1]].append(values)
    result = set({})
    for i in range(W):
        temp[i].sort(reverse=True)
        idx = H - 1
        for j in range(len(temp[i])):
            result.add((idx, temp[i][j][1], temp[i][j][2]))
            idx -= 1
    return result

def bt(bricks, k, n):
    global result
    if k == n:
        result = min(result, len(bricks))
    else:
        if result == 0 or len(bricks) == 0:
            result = 0
            return
        for i in range(W):
            bt(down(bricks - break_brick(i, bricks)), k + 1, n)
            if result == 0:
                return

q = deque()
for T in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    data = []
    data_set = set({})
    for _ in range(H):
        data.append(list(map(int, input().split())))
    for i in range(H):
        for j in range(W):
            if data[i][j] != 0:
                data_set.add((i, j, data[i][j]))
    result = 999999999
    bt(data_set, 0, N)
    print('#{} {}'.format(T, result))