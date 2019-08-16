s1 = 'abc 1, 2, ABC'

s = ''
for i in range(0, len(s1)):
    if s1[i] == '1':
        s = s+'one'
    elif s1[i] == '2':
        s = s+'two'
    else:
        s = s+s1[i]
print(s)