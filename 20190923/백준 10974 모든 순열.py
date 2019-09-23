'''
백준 10974 모든 순열
'''

def next_permutation(a):
    n = len(a) - 1
    i = n
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i == 0:
        return False
    j = n
    while a[i-1] >= a[j]:
        j -= 1
    a[i - 1], a[j] = a[j], a[i - 1]
    j = n
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

a = [i + 1 for i in range(int(input()))]
while True:
    print(' '.join(map(str, a)))
    if next_permutation(a) is False:
        break