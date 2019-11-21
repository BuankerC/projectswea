'''
swea 5688. 세제곱근을 찾아라 D3
'''

for t in range(int(input())):
    N = int(input())
    x = round(N ** (1 / 3), 6)
    x = int(x) if str(x)[-2] == '.' else -1
    print('#{} {}'.format(t+1, x))