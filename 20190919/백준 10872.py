'''
백준 10872 팩토리얼
'''

num = int(input())
res = 1

def factorial(res, count):
    if(num == 0):
        return print(1)
    else:
        res *= count

        if(count == num):
            return print(res)

        return factorial(res, count + 1)
factorial(res, 1)