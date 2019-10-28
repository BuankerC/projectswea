'''
swea 7675 통역사 성경이 D3
'''
import re
for tc in range(int(input())):
    N = int(input())
    talk = re.split('[.?!]', input())[0:N]
    print("#{0}".format(tc+1), end=' ')
    for i in talk:
        cnt = 0
        for j in i.split():
            if j[0].isupper() and j.isalpha():
                if len(j) == 1:
                    cnt += 1
                if j[1:].islower():
                    cnt += 1
        print(cnt, end=' ')
    print('')