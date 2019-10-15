'''
5948. 새샘이의 7-3-5 게임 D3
'''

T = int(input())
for i in range(T):
    num_lst = list(map(int, input().split()))
    result_set = set()
    for a in range(5):
        for b in range(a+1, 6):
            for c in range(b+1, 7):
                num = num_lst[a] + num_lst[b] + num_lst[c]
                result_set.add(num)
    result = sorted(result_set)[-5]
    print('#{} {}'.format(i+1, result))