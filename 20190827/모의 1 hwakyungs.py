def share():
    d = int(input())
    lists = list(map(int, input().split()))
    min_p = min(lists[:-1])
    min_i = lists.index(min_p)
    max_p = max(lists[min_i+1:])
    return max_p - min_p

for tc in range(int(input())):
    print('#{} {}'.format(tc+1,share()))