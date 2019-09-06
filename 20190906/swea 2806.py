'''
swea 2806 N-Queen
'''
def nqueen(depth, n, history):
    global cnt
    if depth == n:
        cnt += 1
    else:
        for i in range(n):
            if i not in history:
                for index, value in enumerate(history):
                    if abs(depth - index) == abs(i - value):
                        break
                else:
                    history.append(i)
                    nqueen(depth + 1, n, history)
                    history.remove(i)


for t in range(int(input())):
    cnt = 0
    nqueen(0, int(input()), [])
    print("#{} {}".format(t+1, cnt))