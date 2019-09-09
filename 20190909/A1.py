# 1부터 5까지 두 그룹으로 나누기
N = 5
# 2진수로 표시해보기
for i in range(1, (1<<N)-1):
    A = []
    B = []
    for j in range(N):
        if (i & (1<<j)) != 0:  # i의 j번 비트가 1이면
            A.append(j+1)
        else:
            B.append(j+1)
    print(A, B)