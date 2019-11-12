'''
swea 8810 당근밭 옆 고구마밭
'''
t = int(input())
for tc in range(1, t + 1):
    N = int(input())
    lines = list(map(int, input().split())) + [0]
    stem = [0] * N
    sweet = [0] * N
    idx = 0
    for i in range(N):
        stem[idx] += 1
        sweet[idx] += lines[i]
        if lines[i + 1] <= lines[i]:
            idx += 1
    cnt = 0
    maxidx = 0
    maxV = 0
    for i in range(N):
        if stem[i] >= 2:
            cnt += 1
            if stem[i] > maxV:
                maxV = stem[i]
                maxidx = i
            elif stem[i] == maxV:
                if sweet[maxidx] < sweet[i]:
                    maxidx = i
    if stem[maxidx] == 1:
        res = 0
    else:
        res = sweet[maxidx]
    print('#{} {} {}'.format(tc, cnt, res))