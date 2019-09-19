'''
백준 8958 OX퀴즈
'''
T = int(input())
list_OX = [input() for _ in range(T)]

for OX in list_OX:
    total_sum = 0
    X_split = OX.split('X')
    for correct in X_split:
        n = len(correct)

        if (n > 0):
            total_sum += (n * (n+1)) // 2
    print(total_sum)