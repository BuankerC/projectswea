'''
swea 2948. 문자열 교집합 D3
'''

for T in range(int(input())):
    N, M = map(int, input().split())
    a = set(list(map(str, input().split())))
    b = set(list(map(str, input().split())))
    print('#{} {}'.format(T + 1, len(a & b)))