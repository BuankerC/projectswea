T = int(input())
for tc in range(1, T+1):
    N = int(input())
    Data = input()
    Data = [int(_) for _ in Data]
    cnt_lst = [0] * 10

    for i in range(N):
        cnt_lst[Data[i]] += 1

    max_index, max_num = 0, 0
    for i in range(len(cnt_lst)-1, -1, -1):
        if cnt_lst[i] > max_index:
            max_index = cnt_lst[i]
            max_num = i

    print('#{} {} {}'.format(tc, max_num, max_index))