'''
swea 1234 [S/W 문제해결 기본] 10일차 - 비밀번호 D3
'''

for t in range(1, 11):
    N, S = input().split()
    stk = []
    for i in range(int(N)):
        if stk == [] or stk[-1] != S[i]:
            stk.append(S[i])
        elif stk[-1] == S[i]:
            stk.pop()
    print('#{} {}'.format(t, ''.join(stk)))