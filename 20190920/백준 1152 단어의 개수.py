'''
백준 1152 단어의 개수
'''
string = input('')
words = string.split(' ')
words = [w for w in words if w != '']
print(len(words))