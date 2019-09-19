'''
백준 1546 평균
'''

a = int(input())
b = list(map(int, input().split()))
c = 0
jujak = []
for i in b:
    c += i

average = c / a

for i in b:
    jujak.append(i/max(b) * 100)

print('%0.2f' % (sum(jujak) / a))