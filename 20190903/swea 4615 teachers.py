def find(N, stone, o): # r,c 부터 뒤집을 수 있는 경우 찾아 뒤집기
    dr = [ 0, 1, 1, 1, 0, -1, -1, -1 ] # 오른쪽부터 시계방향
    dc = [ 1, 1, 0, -1, -1, -1, 0, 1 ]
    o[N//2][N//2] = 2
    o[N//2][N//2+1] = 1
    o[N//2+1][N//2] = 1
    o[N//2+1][N//2+1] = 2
    for s in stone:
        r = s[0]
        c = s[1]
        z = s[2]
        o[r][c] = z
        bw = 1 if z==2 else 2 # z와 반대돌
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            flip = 0
            while(nr>=1 and nr<=N and nc>=1 and nc<=N and o[nr][nc] == bw):
                nr += dr[i]
                nc += dc[i]
                flip = 1
            if(nr>=1 and nr<=N and nc>=1 and nc<=N and o[nr][nc]==z):
                if(flip==1): # 다시 z 색이 나오면
                    nr = r + dr[i]
                    nc = c + dc[i]
                    while(o[nr][nc] == bw):
                        o[nr][nc] = z
                        nr += dr[i]
                        nc += dc[i]
    return o

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    o = [[0]*(N+1) for i in range(N+1)]
    stone = [list(map(int, input().split())) for i in range(M)]
    o = find(N, stone, o)
    B = 0
    W = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if(o[i][j] == 1):
                B += 1
            elif(o[i][j] == 2):
                W += 1
    print('#{} {} {}'.format(tc, B, W))