'''
백준 2751 수 정렬하기 2
'''
import sys

n = int(input())
sample1 = []
sample2 = []

for i in range(n):
    sample = int(sys.stdin.readline())
    if i % 2 == 0:
        sample1.append(sample)
    else:
        sample2.append(sample)

sample1.sort(reverse=True)
sample2.sort(reverse=True)

try:
    for i in range(n):
        if sample1[-1] < sample2[-1]:
            print(sample1.pop())
        else:
            print(sample2.pop())
except:
    if len(sample1) == 0:
        for i in range(len(sample2)):
            print(sample2.pop())
    else:
        for i in range(len(sample1)):
            print(sample1.pop())