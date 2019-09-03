'''

swea 1221. GNS

'''

numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
def find_index(word):
    idx = -1
    for i in range(10):
        if word == numbers[i]:
            idx = i
            break
    return idx

tc = int(input())
for _ in range(1, tc+1):
    a, b = input().split()
    n = int(b)
    arr = list(input().split())

    count = [0] * 10
    for i in range(n):
        count[ find_index(arr[i]) ] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    res = [0] * n
    for i in range(n-1, -1, -1):
        res[count[ find_index(arr[i]) ] - 1] = arr[i]
        count[ find_index(arr[i]) ] -= 1

    print(f'{a}\n' + ' '.join(res))
