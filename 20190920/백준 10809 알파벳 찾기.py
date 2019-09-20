'''
백준 10809 알파벳 찾기
'''
abc = 'abcdefghijklmnopqrstuvwxyz'
word_list = []
word_num = []

word = str(input())

for i in word:
    word_list.append(i)

for char in abc:
    for i in range(len(word_list)):
        if char == word_list[i]:
            word_num.append(i)
            break
        elif i < len(word_list) - 1:
            continue
        else:
            word_num.append(-1)
for i in word_num:
    print(i, end=' ')