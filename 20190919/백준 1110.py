'''
백준 1110 더하기 사이클
'''
num = int(input())
check = num
new_num = 0
temp = 0
cnt = 0
while True:
    temp = num // 10 + num % 10
    new_num = (num % 10) * 10 + temp % 10
    cnt += 1
    num = new_num
    if new_num == check:
        break
print(cnt)