arr = [[0]*4 for i in range(3)]
print(arr)
# 행과 열이 같은 칸을 기준으로 우측 영역
k = 1
for i in range(4):
    for j in range(4):
        if (i<j):
            arr[i][j] = k
            k = k + 1
print(arr)
# 행과 열이 같은 칸을 기준으로 좌측 영역
k = 10
for i in range(4):
    for j in range(4):
        if (i>j):
            arr[i][j] = k
            k = k + 10
print(arr)