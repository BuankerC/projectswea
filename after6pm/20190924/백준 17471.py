'''
백준 17471 게리맨더링
'''

def bfs(area, N):
    q = [area[0]]
    v = [0]*(N+1)
    v[area[0]] = 1
    total = 0
    while(len(q)!=0):
        i = q.pop(0)
        total += p[i]
        for j in area:
            if adj[i][j] == 1 and v[j] ==0:
                q.append(j)
                v[j] = v[i] + 1
    for i in area:
        if v[i] == 0:
            return 0
    return total

N = int(input())
p = [0] + list(map(int, input().split()))
adj = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    node = list(map(int, input().split()))
    for j in node[1:]:
        adj[i][j] = 1
        adj[j][i] = 1

minV = 1000000000
for i in range(1, (1<<N)//2):
    areaA = []
    areaB = []
    for j in range(N):
        if i&(1<<j) !=0:
            areaA.append(j+1)
        else:
            areaB.append(j+1)
    rA = bfs(areaA, N)
    rB = bfs(areaB, N)
    if rA*rB != 0:
        if minV>abs(rA-rB):
            minV = abs(rA-rB)
if minV == 1000000000:
    minV = -1

print(minV)