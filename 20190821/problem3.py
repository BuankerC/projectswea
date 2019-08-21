N =int(input())
arr = [list(map(int, input().split())) for _ in range(N)] # 2차원 배열 만들기?!
cnt = 0
for i in range(N): # 행을 지정
    for j in range(N): # 열을 지정
        if arr[i][j] % 2 == 0 : # 짝수인 경우
            cnt += 1
print(cnt)
​
# 응용
# 짝수가 가장 많은 행은? (0번행부터 시작)
# 한 행에 최대 몇 개의 짝수가 존재하는가?
# 짝수 중 가장 큰 값은?