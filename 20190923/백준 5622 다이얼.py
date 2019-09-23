'''
백준 5622 다이얼
'''

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
a = input()
res = 0
for j in range(len(a)):
    for i in dial:
        if a[j] in i:
            res += dial.index(i) + 3
print(res)