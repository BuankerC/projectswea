tc = int(input())
for t in range(1, tc + 1):
    step = list(input())
    tmp = ['0'] * len(step)
    cnt = 0
    for i in range(len(step)):
        if step[i] != tmp[i]:
            cnt += 1
            for j in range(i, len(step)):
                tmp[j] = step[i]
    print('#{} {}'.format(t, cnt))