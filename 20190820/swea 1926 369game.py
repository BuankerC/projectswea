# N = int(input())
#
# for i in range(1, N + 1):
#     a = str(i).count('3') + str(i).count('6') + str(i).count('9')
#     if a:
#         print('-'*a, end='')
#     else:
#         print('-', end='')
n = int(input())
forbid = ['3', '6', '9']
for i in range(1, n+1):
    forbid_count = 0
    for j in str(i):
        if j in forbid:
            forbid_count += 1
    if forbid_count == 0:
        print(i, end=" ")
    else:
        print('-'*forbid_count, end=" ")