def f(n, v, arr):
    for idx in range(0, n):
        if (arr[idx]==v): # 키 값을 찾으면 중단
            return idx
    return -1  # 배열 안에서 키 값을 찾지 못하면

# 개수 N, 키 V
N, V = map(int, input().split())
arr = list(map(int, input().split()))
r = f(N, V, arr)
print(r)





