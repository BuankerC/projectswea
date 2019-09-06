'''
swea 3499 퍼펙트 셔플 D3
'''

tc = int(input())
for t in range(1, tc+1):
    n = int(input())
    cards = input().split()
    h = 0
    if n % 2 == 0:
        h = (n // 2)
    else:
        h = (n // 2) + 1

    c1 = cards[:h]
    c2 = cards[h:]

    s = []
    for i in c1:
        s.append(i)
        if len(c2) != 0:
            s.append(c2[0])
            c2.pop(0)

    print("#%d "%(t), end='')
    for i in s:
        print(i+' ', end='')
    print()