'''
백준 2750 수 정렬하기
'''

depth = int(input())

array = list()

for i in range(depth):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)