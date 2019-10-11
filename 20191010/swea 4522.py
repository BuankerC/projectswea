'''
swea 4522. 세상의 모든 팰린드롬 D3
'''

t = int(input())

for tc in range(1, t + 1):
    word = input()
    n = len(word)

    i = 0
    while i <= n // 2 - 1:
        if word[i] == word[n - 1 - i]:
            i += 1
        elif word[i] == '?' or word[n - 1 - i] == '?':
            i += 1
        else: # 팰린드롬 아니면,
            print('#{} Not exist'.format(tc))
            break
    else: # 팰린드롬
        print('#{} Exist'.format(tc))