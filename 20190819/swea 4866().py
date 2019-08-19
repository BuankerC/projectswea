TC = int(input())
for tc in range(1, TC+1):
    Data = input()
    N = len(Data)
    stack = []
    for i in range(N):
        #여는 괄호가 올 경우 => stack에 저장
        if Data[i] == '(' or Data[i] == '{':
            stack.append(Data[i])
        elif Data[i] == ')' or Data[i] == '}':
            #닫는 괄호이며 stack이 빈 경우 => 처음부터 닫는 괄호가 오는 경우
            if len(stack) == 0:
                stack = [Data[i]]
                break
            #stack에 저장된 괄호와 일치하지 않는 경우
            elif (Data[i] == '}' and stack[-1] !='{') or (Data[i] == ')' and stack[-1] != '('):
                stack = [Data[i]]
                break
            #stack에 저장된 괄호와 일치하는 닫는 괄호가 오는 경우
            else:
                stack.pop()

    if not len(stack):
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')