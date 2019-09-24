'''
백준 1193 분수찾기
'''

x = int(input())

cnt = 0

while x > 0:
    x -= cnt
    cnt += 1

x = cnt + x - 1

ans = str(x) + '/' + str(cnt - x)
if cnt % 2 == 0:
    ans = str(cnt - x) + '/' + str(x)
print(ans)