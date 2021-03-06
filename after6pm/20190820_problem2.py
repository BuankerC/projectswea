# 문제2
# 산책길을 따라 N개 지점의 높이를 기록한 표를 만들었다. 산책길은 오르막 혹은 내리막으로 이뤄져 있고 오르막에서 내리막으로 바뀌는 부분을 봉우리라고 부르기로 했다. 주어진 산책로 정보에서 몇 개의 봉우리가 있는지 출력하는 프로그램을 만드시오. 맨 처음과 마지막 지점은 봉우리인지 판단할 수 없다.
#
# 첫 줄에 N, 다음 줄에 1000 이하인 N개의 양의 정수가 주어진다.
#
# 입력1
#
# 10
#
# 7 2 3 4 1 2 5 4 5 6
#
# 출력 1
#
# 2
#
# 입력 2
#
# 7
#
# 1 2 1 2 1 2 1
#
# 출력 2
#
# 3
#
# [생각해보기]
#
# 골짜기의 개수는?
# 봉우리 사이에 다리를 놓으려 한다. 가장 긴 다리의 길이는? 봉우리가 한 개인 경우 0을 출력한다.

T = int(input())
arr = list(map(int, input().split()))
down = 0
cnt = 0
for i in range(0, T-1):
    if arr[i-1] <= arr[i]:
        if down == 1:
            cnt += 1
            down = 0
    else:
        down = 0

print(cnt)