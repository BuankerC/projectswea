T = int(input())
for t in range(1, T + 1):
    N, D = map(int, input().split())
    gate = [1] + list(map(int, input().split()))
    i = 0
    cnt = 0
    out = False
    while 1:
        temp = []
        for j in range(1, D + 1):
            if i + j > N:
                out = True
                break
            if gate[i+j] == 1:
                temp.append(i + j)
        if out:
            break
        if temp == []:
            i = i + D
            cnt += 1
        else:
            i = temp[-1]
        if i > N:
    please(cnt)