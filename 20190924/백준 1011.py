'''
백준 1011 Fly me to the Alpha Centauri
'''

case_num = int(input())
ans = []
for i in range(case_num):
    a, b = map(int, input().split())
    num = b - a
    k = 1
    p = 1
    while num > 0:
        num -= k
        k += 1
        if num >= p:
            num -= p
            p += 1

    ans.append(k+p-2)

for i in ans:
    print(i)