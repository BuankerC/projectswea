'''
백준 2839 설탕 배달
'''
# 숏코딩
# order = int(input())
# three = 0
# five = order // 5
# order %= 5
#
# while five >= 0:
#     if order % 3 == 0:
#         three = order // 3
#         order %= 3
#         break
#     five -= 1
#     order += 5
# print(order==0 and (three + five) or -1)

order = int(input())

if order % 5 == 0:
    print(order // 5)

elif order % 5 == 3:
    print(order // 5 + 1)

elif order // 5 - 1 >= 0 and order - (5 * (order // 5 - 1)) == 6:
    print((order // 5 - 1) + 2)

elif order // 5 - 1 >= 0 and order - (5 * (order // 5 - 1)) == 9:
    print((order // 5 - 1) + 3)

elif order // 5 - 2 >= 0 and order - (5 * (order // 5 - 2)) == 12:
    print((order // 5 - 2) + 4)

else:
    print(-1)