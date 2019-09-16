'''
swea 1248. [S/W 문제해결 응용] 3일차 - 공통조상 D5
'''


def getsize(node):
    global size
    if node != 0:
        size += 1
        if pchild[node] != []:
            getsize(pchild[node][0])
            if len(pchild[node]) > 1:
                getsize(pchild[node][1])


for case in range(1, int(input()) + 1):
    nodeNum, edgeNum, target1, target2 = map(int, input().split())
    edgeinfo = list(map(int, input().split()))
    pchild = [[] for i in range(nodeNum + 1)]
    cparent = [0] * (nodeNum + 1)
    for i in range(len(edgeinfo)):
        if i % 2 == 0:
            parent = edgeinfo[i]
        else:
            child = edgeinfo[i]
            pchild[parent].append(child)
            cparent[child] = parent
    target1ances, target2ances = [], []
    t = target1
    while cparent[t] != 0:
        target1ances.append(cparent[t])
        t = cparent[t]
    t = target2
    while cparent[t] != 0:
        target2ances.append(cparent[t])
        t = cparent[t]
    result = 0
    for t1 in target1ances:
        for t2 in target2ances:
            if t1 == t2:
                result = t1
                break
        if result != 0:
            break
    size = 0
    getsize(result)
    print('#{} {} {}'.format(case, result, size))