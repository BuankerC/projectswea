for tc in range(1, 11):
    tc = int(input())
    N = 100
    result = 1

    # 가로줄 확인
    Garo_lst = []
    for i in range(N):
        Data = input()
        Garo_lst.append(Data)
        #회문 길이
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if Data[k:M+K] == Data[k:M+K][::-1]:
                    if len(Data[k:M+k]) > result:
                        result = len(Data[k:M+k])

    # 세로줄 확인
    Sero_lst = []
    Sero_sub_lst = ''
    for x in range(N):
        for y in Garo_lst:
            Sero_lst.append(Sero_sub_lst)
            Sero_sub_lst = ''

    for sero_data in Sero_lst:
        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if sero_data[k:M+k] == sero_data[k:M+k][::-1]:
                    if len(sero_data[k:M+k]) > result:
                        result = len(sero_data[k:M+k])

    print("#%d %s"%(tc, result))