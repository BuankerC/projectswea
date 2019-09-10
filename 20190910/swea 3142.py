'''
swea 3142 영준이와 신비한 뿔의 숲 D3
2x + y = N
x + y = M
y = M - x
2x + M - x = N
=> x = N - M (트윈혼)
=> y = 2M - N (유니콘)
'''

for t in range(int(input())):
    N,M = map(int,input().split())
    print('#{} {} {}'.format(t+1,2*M-N,N-M))