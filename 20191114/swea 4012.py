'''
swea 4012. [모의 SW 역량테스트] 요리사
'''
arr = [n for n in range(16)]
for T in range(1, int(input())+1):
    N = int(input())
    s = []
    for _ in range(N):
        s.append(list(map(int, input().split())))
    food = []
    for i in range(1 << N):
        cnt = 0
        temp = []
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                temp.append(arr[j])
        if cnt == N // 2:
            food.append(temp)
    result = 9999999999
    for case in food:
        Sum1 = 0
        Sum2 = 0
        for i in range(N):
            for j in range(N):
                if i in case and j in case:
                    Sum1 += s[i][j]
                elif i not in case and j not in case:
                    Sum2 += s[i][j]
        result = min(result, abs(Sum1 - Sum2))
    print('#{} {}'.format(T, result))