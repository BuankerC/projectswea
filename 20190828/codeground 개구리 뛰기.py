T = int(input())
for tc in range(1, T + 1):
K, N = map(int, input().split())
stone = list(map(int, input().split()))
stop = [0] * (N + 1)

for i in stone:
    stop[i] = 1
    