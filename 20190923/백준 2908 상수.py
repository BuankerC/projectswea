'''
백준 2908 상수
'''
a, b = input().split()

rev_a = int(a[::-1])
rev_b = int(b[::-1])

print(max(rev_a, rev_b))