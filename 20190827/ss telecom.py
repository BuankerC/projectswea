def cover(i, j, N):
    k = 0
    if arr[i][j] == 'A':
        k = 1
    elif arr[i][j] == 'B':
        k = 2
    elif arr[i][j] == 'C':
        k = 3
    for h in range(1, k+1): # 방향별로 순환
        if(j+h<N):
            arr[i][j+h] = 'X' # 오른쪽
        if(i+h<N):
            arr[i+h][j] = 'X' # 아래
        if(i+h<N):
            arr[i][j-h] = 'X' # 왼쪽
        if(i-h<N):
            arr[i-h][j] = 'X' # 위

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 기지국과 집 정보 입력
    arr = [list(input()) for _ in range(N)]
    # 기지국 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A' or 'B' or 'C':

                # 커버되는 집 찾기
                cover(i, j, N)

    # 남은 집 개수 세기
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1
    print('#{} {}'.format(tc, cnt))



