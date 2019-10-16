'''
swea 6692. 다솔이의 월급 상자 D3
'''

T = int(input())
for i in range(T):
    N = int (input())
    moneylst = []
    for j in range(N):
        p, m = map(float, input().split())
        money = p * m
        moneylst.append(money)
    result = sum(moneylst)
    print('#{} {:.6f}'.format(i+1, result))