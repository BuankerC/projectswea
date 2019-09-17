'''
백준 1182. 부분수열의 합
'''
import sys
import itertools

N, S = map(int, input().split())
num = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in range(1, N + 1):
    boxes = itertools.combinations(num, i)

    for box in boxes:
        if sum(box) == S:
            cnt += 1
print(cnt)