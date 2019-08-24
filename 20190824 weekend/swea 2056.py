t = int(input())
for i in range(1, t+1):
    test = input()

    m1 = ['01', '03', '05', '07', '08', '10', '12']
    m2 = ['04', '06', '09', '11']
    if (test[4:6] in m1) and 1 <= int(test[6:]) <= 31:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    elif test[4:6] == '02' and 1 <= int(test[6:]) <= 28:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    elif (test[4:6] in m2) and 1 <= int(test[6:]) <= 30:
        print(f'#{i} {test[0:4]}/{test[4:6]}/{test[6:8]}')
    else:
        print(f'#{i} -1')