'''
백준 1712 손익 분기점
'''
A, B, C = map(int, input().split())

sales = 0

if B < C:
    sales = A // (C - B)
    print(sales + 1)

else:
    print(-1)