N, K = map(int, input().split())
arr = list(map(int, input().split()))

i = 0
cntK = 0
while(i<N):
    while(i < N and arr[i] == 0):
        i += 1
    cnt = 0
    while(i < N and arr[i] == 1):
        cnt += 1
        i += 1
    if cnt == K:
        cntK += 1
print(cntK)
