def find():
    dRow = [0,1,0,-1]
    dCol = [1,0,-1,0]
    s = []
    s.append([sRow,sCol])  # 입구로 이동
    maze[sRow][sCol] = 1   # 방문 표시
    while(len(s)!=0):
        n = s.pop()        # 이동할 칸 좌표를 꺼내고
        for i in range(4): # 주변 좌표 계산
            nRow = n[0] + dRow[i]
            nCol = n[1] + dCol[i]
            if nRow >= 0 and nRow < N and nCol >= 0 and nCol < N: # 미로 내부인지 확이
                if maze[nRow][nCol] == 3:   # 목적지인 경우 1 반환
                    return 1
                elif maze[nRow][nCol] == 0:     # 갈 수 있는 곳 저장
                    s.append([nRow, nCol])
                    maze[n[0]][n[1]] = 1
    return 0        #출구에 가지 못하고 모든 칸 방문