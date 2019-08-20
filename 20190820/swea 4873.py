T = int(input())
for tc in range(1, T+1):
    txt = input()
    s = list()
    s.append(txt[0])
    for i in range(1, len(txt)):
        # 스택의 맨 위 글자와 다르면 push(txt[i]), 다르면 pop()
        if len(s) == 0 or s[-1] != txt[i]:
            s.append(txt[i])
        else:
            s.pop()
    print('#{} {}'.format(tc, len(s)))