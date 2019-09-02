def find(si, sj, N):
    global arr
    row, col = 1, 1
    ni, nj = si, sj
    for _ in range(N):
        ni += 1
        if ni < N and arr[ni][sj]:
            row += 1
        else:
            break
    for _ in range(N):
        nj += 1
        if nj < N and arr[si][nj]:
            col += 1
        else:
            break
    for i in range(si, ni):
        for j in range(sj, nj):
            arr[i][j] = 0
    return row, col
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                result.append(find(i, j, N))
    result = sorted(result, key=lambda x: (x[0] * x[1], x[0]))
    print('#{} {}'.format(tc, len(result)), end=' ')
    for i in result:
        print(i[0], i[1], end=' ')
    print()