N = int(input())
arr = list(map(int, input().split())) # arr: <class 'list'>: [2, 38, 65, 68, 69, 72, 80, 85, 96]

for i in range(N-1, 0, -1): # 정렬 구간의 마지막 인덱스
    for j in range(0, i):
        if(arr[j] > arr[j+1]):
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp
print(arr[N//2])