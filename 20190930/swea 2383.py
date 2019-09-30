'''
swea 2383. [모의 SW 역량테스트] 점심 식사시간
'''

from copy import deepcopy
from collections import deque

def do():
    global N
    time = [0, 0]
    for i in range(2):
        tmp = deepcopy(stairs[i])
        dis = [0] * len(tmp)
        for j in range(len(tmp)):
            dis[j] = abs(tmp[j][0] - stair[i][0]) + abs(tmp[j][1] - stair[i][1])
        dis.sort()
        q = deque()
        while dis or q:
            time[i] += 1
            len_q = len(q)
            for j in range(len_q):
                t = q.popleft()
                t -= 1
                if t:
                    q.append(t)
            len_dis = len(dis)
            for j in range(len_dis):
                if len(q) < 3 and time[i] > dis[0]:
                    dis.pop(0)
                    q.append(stair[i][2])
                else:
                    break
    return max(time)

def dfs(n):
    global N, p_cnt, result
    if n == p_cnt:
        t = do()
        if t < result:
            result = t
        return
    for i in range(2):
        stairs[i].append(people[n])
        dfs(n + 1)
        stairs[i].pop()

for tc in range(1, int(input()) + 1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stair = []
    stairs = [[], []]
    p_cnt = 0
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                p_cnt += 1
                people.append([i, j])
            elif m[i][j]:
                stair.append([i, j, m[i][j]])
    result = 1000000000
    dfs(0)
    print('#{} {}'.format(tc, result))