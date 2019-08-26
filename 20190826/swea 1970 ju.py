charges = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T + 1):
    result = []
    money = int(input())
    for charge in charges:
        mok = money // charge
        result.append(mok)
        money -= mok*charge

    print('#{}'.format(tc))
    for i in result:
        print(i, ends=' ')
    print('')