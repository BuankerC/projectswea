for i in range(int(input())):
    exchange = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{i+1}')
    for j in money:
        if exchange // j == 0:
            print(0, end=" ")
        elif exchange // j >= 1:
            print(exchange // j, end=" ")
            exchange %= j
    print()