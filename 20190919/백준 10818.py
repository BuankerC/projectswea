'''
백준 10818 최소, 최대
'''

N = int(input())
Nlist = list(map(int, input().split()))
print('{} {}'.format(min(Nlist), max(Nlist)))