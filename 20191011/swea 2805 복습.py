'''
swea 2805. 농작물 수확하기 D3
'''

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, list(input())))

    ans = 0
    M = N // 2
    for i in range(M):
        ans += sum(mat[i][M-i:M+i+1])
    ans += sum(mat[M])
    for i in range(M-1, -1, -1):
        ans += sum(mat[N-1-i][M-i:M+i+1])
    print('#{} {}'.format(t, ans))