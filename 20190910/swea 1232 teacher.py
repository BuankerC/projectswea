# 완전 이진트리로 보고 접근

operator = ['+', '-', '*', '/']

def f(n, last):
    if tree[n] in operator:
        r1 = f(ch1[n], last)
        r2 = f(ch2[n], last)
        if tree[n] == '+':
            return r1 + r2
        elif tree[n] == '-':
            return r1 - r2
        elif tree[n] == '*':
            return r1 * r2
        elif tree[n] == '/':
            return r1 / r2
    else:
        return int(tree[n])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for i in range(N):
        node = list(input().split())
        if len(node) > 2:
            tree[int(node[0])] = node[1]
            ch1[int(node[0])] = int(node[2])
            ch1[int(node[0])] = int(node[3])

    r = f(1, N)
    print('#{} {}'.format(tc, int(r)))