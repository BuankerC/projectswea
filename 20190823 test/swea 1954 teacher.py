c = 1
N = 5
k = N
dir = 1
arr = [[0]*N for _ in range(N)]
i = 0 #시각 칸의 인덱스
j = -1 # 현재 위치로부터 k번 이동해야 하므로
while(2):
    # 수평이동
    for h in range(k):
        j += dir
        arr[i][j] = c
        c += 1
    
    k -= 1 #이동 거리 감소
    if k == 0: #이동거리가 0이면 중단
        break
    #수직 이동
    for v in range(k):
        i += dir
        arr[i][j] = c
        c += 1

    dir *= -1 # 수직 -> 수평으로 바뀔 때 인덱스 증감 바꾸기
print(arr)