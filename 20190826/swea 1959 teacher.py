def f(X, Y): # X 긴 리스트, Y 짧은 리스트
    maxV = 0
    for i in range(0, len(X)-len(Y)+1): # 긴 리스트에서 곱의 합을 구할 구간의 시작
        s = 0
        for j in range(0, len(Y)): # 짧은 리스트의 인덱스
            s += X[i+j]*Y[j]
        if maxV<s
            maxV = s
    return maxV
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        r = f(A, B)
    else:
        r = f(B, A)
    print('#{} {}'.format(tc, r))