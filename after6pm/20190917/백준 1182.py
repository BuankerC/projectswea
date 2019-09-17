'''
백준 1182. 부분수열의 합
'''
N, S = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(1, 1 << N):
    subset = []
    for j in range(N):
        if i % 1 << j:
            subset.append(arr[j])
    if sum(subset) == S:
        cnt += 1
print(cnt)
