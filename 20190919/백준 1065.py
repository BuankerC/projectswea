'''
백준 1065 한수
'''

num = int(input())
numberlist = []

for k in range(1, num + 1):
    if 0< k < 100:
        numberlist.append(k)
    elif 100 <= k < 1000:
        number_shape = []
        number_shape = [k // 100, (k // 10) % 10, k % 10]
        if number_shape[0] - number_shape[1] == number_shape[1] - number_shape[2]:
            numberlist.append(k)

    elif num == 1000:
        break

print(len(numberlist))