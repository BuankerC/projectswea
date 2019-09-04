'''
swea 6109. 추억의 2048 게임 D4
'''

T = int(input())
for t in range(1, T + 1):
    data = input().split()
    N = int(data[0])
    word = data[1]
    new = [[0] * N for _ in range(N)]
    data = [list(map(int, input().split())) for _ in range(N)]

    if word == 'up':
        for j in range(N):
            i = blank = 0
            stack = []
            while i < N:
                # 0이 아닌 경우
                if data[i][j]:
                    stack.append(data[i][j])
                    i += 1
                    if len(stack) > 1:
                        if stack[0] == stack[1]:
                            new[blank][j] = stack.pop() + stack.pop()
                            blank += 1
                        else:
                            new[blank][j] = stack.pop(0)
                            blank += 1
                else:
                    i += 1
                if i == N and stack:
                    for find in range(blank, N):
                        if new[find][j] == 0 and stack:
                            new[find][j] = stack.pop(0)
    elif word == 'down':
        for j in range(N):
            i = blank = N - 1
            stack = []
            while i > -1:
                # 0이 아닌 경우
                if data[i][j]:
                    stack.append(data[i][j])
                    i -= 1
                    if len(stack) > 1:
                        if stack[0] == stack[1]:
                            new[blank][j] = stack.pop() + stack.pop()
                            blank -= 1
                        else:
                            new[blank][j] = stack.pop(0)
                            blank -= 1
                else:
                    i -= 1
                if i == -1 and stack:
                    for find in range(blank, -1, -1):
                        if new[find][j] == 0 and stack:
                            new[find][j] = stack.pop(0)
    elif word == 'left':
        for i in range(N):
            j = blank = 0
            stack = []
            while j < N:
                # 0이 아닌 경우
                if data[i][j]:
                    stack.append(data[i][j])
                    j += 1
                    if len(stack) > 1:
                        if stack[0] == stack[1]:
                            new[i][blank] = stack.pop() + stack.pop()
                            blank += 1
                        else:
                            new[i][blank] = stack.pop(0)
                            blank += 1
                else:
                    j += 1
                if j == N and stack:
                    for find in range(blank, N):
                        if new[i][find] == 0 and stack:
                            new[i][find] = stack.pop(0)
    elif word == 'right':
        for i in range(N):
            j = blank = N - 1
            stack = []
            while j > -1:
                # 0이 아닌 경우
                if data[i][j]:
                    stack.append(data[i][j])
                    j -= 1
                    if len(stack) > 1:
                        if stack[0] == stack[1]:
                            new[i][blank] = stack.pop() + stack.pop()
                            blank -= 1
                        else:
                            new[i][blank] = stack.pop(0)
                            blank -= 1
                else:
                    j -= 1
                if j == -1 and stack:
                    for find in range(blank, -1, -1):
                        if new[i][find] == 0 and stack:
                            new[i][find] = stack.pop(0)
    print('#{}'.format(t))
    for res in new:
        print(' '.join(map(str, res)))