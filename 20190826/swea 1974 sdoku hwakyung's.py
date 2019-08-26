for tc in range(int(input())):
    lists = [list(map(int, input().split())) for _ in range(9)]
    lists_r = list(zip(*lists)) # zip은 세로로 배열 정렬
    count = 1
    for i in range(9):
        if len(set(lists[i])) != 9:
            count = 0
            break
        if len(set(lists_r[i])) != 9:
            count = 0
            break
    result = []
    for i in range(0, 9, 3):
        res = 0
        for j in range(3):
            res += sum(lists[i+j][i:i+3])
        if res != 45
            count = 0
            break
    print(f'#{tc+1} {count}')