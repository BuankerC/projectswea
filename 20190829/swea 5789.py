'''
swea 5789 현주의 상자 바꾸기 D3
'''
for t in range(int(input())):
    N, Q = map(int, input().split())
    ans = ['0'] * N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            ans[j] = str(i+1)
    print(f"#{t+1} {' '.join(ans)}")