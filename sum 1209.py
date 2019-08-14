TC = 10
for tc in range(1, TC+1):
    lst = []
    N = int(input())
    for i in range(100):
        sub_lst = list(map(int, input().split()))
        lst.append(sub_lst)

    result = []

    for y in range(len(lst)): #각 행의 합
        sum_row = 0
        for x  in range(len(lst)):
            sum_row += lst[y][x]
        result.append(sum_row)

    for x in range(len(lst)): #각 열의 합
        sum_col = 0
        for y in range(len(lst)):
            sum_col += lst[y][x]
        result.append(sum_col)

    sum_diagonal1 = 0
    for y in range(len(lst)):   #첫번째 대각선의 합
        for x in range(len(lst)):
            if y == x:
                sum_diagonal1 += lst[y][x]
    result.append(sum_diagonal1)

    sum_diagonal2 = 0
    for y in range(len(lst)): #두번쨰 대각선의 합
        for x in range(len(lst)):
            if y == len(lst)-x:
                sum_diagonal2 += lst[y][x]
    result.append(sum_diagonal2)

    print(f'#{tc} {max(result)}')