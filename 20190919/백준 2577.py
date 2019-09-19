'''
백준 2577 숫자의 개수
'''
a = int(input())
b = int(input())
c = int(input())

k = a * b * c
k_lst = list(str(k))
for i in range(10):
    k_num_cnt = k_lst.count(str(i))
    print(k_num_cnt)