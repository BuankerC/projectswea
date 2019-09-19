'''
swea 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용 D3
'''

def solve(i, cnt):
    global mins
    if i == N:
        if cnt < mins:
            mins = cnt
        return
    for j in range(N):
        if not chk[j] and cnt + mat[i][j] <= mins:
            chk[j] = 1
            solve(i + 1, cnt + mat[i][j])
            chk[j] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))
    chk = [0] * N
    mins = 1500
    solve(0, 0)
    print('#{} {}'.format(tc, mins))