'''
swea 5174 subtree D2
'''

def preorder_count(root):
    global cnt
    if root:
        cnt += 1
        preorder_count(tree[root][0])
        preorder_count(tree[root][1])
tc = int(input())
for t in range(1, tc+1):
    cnt = 0
    E, N = map(int, input().split())
    tree = [[0, 0] for _ in range(E+2)]
    arr = [int(n) for n in input().split()]
    for i in range(len(arr) // 2):
        p, c = arr[i*2], arr[i*2+1]
        if not tree[p][0]:
            tree[p][0] = c
        else:
            tree[p][1] = c
    print(f'#{t}', end=' ')
    preorder_count(N)
    print(cnt)