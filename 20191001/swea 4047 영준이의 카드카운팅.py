'''
swea 4047 영준이의 카드 카운팅
'''
T = int(input())
for tc in range(T):
    data = str(input())
    count, ans = [13, 13, 13, 13], []
    x, y = 0, 0

    while y < len(data):
        y += 3
        ans.append(data[x:y])
        x = y
    if len(ans) != len(list(set(ans))):
        print('#{} {}'.format(tc+1, 'ERROR'))
        continue
    else:
        for k in ans:
            if k[0] == 'S': count[0] -= 1
            if k[0] == 'D': count[1] -= 1
            if k[0] == 'H': count[2] -= 1
            if k[0] == 'C': count[3] -= 1
    print('#{} '.format(tc+1,), end='')
    print(*count)