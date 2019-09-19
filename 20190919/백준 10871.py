'''
백준 10871 - X보다 작은 수
'''

count, num = map(int, input().split())
inArr = list(map(int, input().split()))
for i in range(count):
    if inArr[i] < num:
        print(inArr[i], end=' ')