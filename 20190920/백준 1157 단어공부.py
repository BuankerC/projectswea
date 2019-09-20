'''
백준 1157 단어공부
'''

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

word = str(input()).upper()
char_maxnum = 0

for char in abc:
    char_num = word.count(char)
    if char_num > char_maxnum:
        char_maxnum = char_num

max_abc = []
for char in abc:
    if word.count(char) == char_maxnum:
        if max_abc:
            max_abc.append(char)
            print('?')
            break
        else:
            max_abc.append(char)

if len(max_abc) == 1:
    print(max_abc[0])