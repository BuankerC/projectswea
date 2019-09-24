N = int(input())

for i in range(1, (1 << N) // 2):  # 비트 연산으로 두 그룹으로 나눔, 절반만 선택하면 나머지는 다른 그룹에 속함
    areaA = []
    areaB = []
    for j in range(N):
        if i & (1 << j) != 0:
            areaA.append(j + 1)
        else:
            areaB.append(j + 1)
    print(areaA, areaB)