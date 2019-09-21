'''
swea 3233 정삼각형 분할놀이 D3
'''
for a in range(int(input())):
    A, B = map(int, input().split())
    n = A // B
    result = 0
    element = 1
    for _ in range(n):
        result += element
        element += 2
    print('#{} {}'.format(a + 1, result))