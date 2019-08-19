TC = int(input())

for tc in range(1, TC+1):
    Data = list(input())
    N = len(Data)
    stack = []
    for i in range(N):
        # stack이 비었거나, 스택의 마지막 값이 데이터 내 값과 같지 않은 경우
        # stack에 저장(append)
        if not stack or stack[-1] != Data[i]:
            stack.append(Data[i])
        #stack에 값이 있고, 스택의 마지막 값과 데이터 내 값과 같은 경우
        # stcak에서 제거(pop)
        elif stack and stack[-1] == Data[i]:
            stack.pop()
    print(f'#{tc} {len(stack)}')