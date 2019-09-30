def check(i, t):


def f(k, pcnt):
    t0 = [0] * 200  # 시간별로 계단에 머무는 사람 수 기록
    t1 = [0] * 200
    for i in range(pcnt):  # i번 사람이 어느 계단으로 갈지 결정
        if k & (1 << j):  # 0번 계단으로 가는 경우
            check(i, 0)
        else:  # 1번 계단으로 가는 경우
            check(i, 1)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    m = [list(map(int, input().split())) for _ in range(N)]
    person = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                person.append([i, j])
            elif m[i][j] != 0:
                stairs.append([i, j, m[i][j]])
    dis = [[0] * 2 for i in range(len(person))]
    for i in range(len(person)):
        dis[i][0] = abs(person[i][0] - stairs[0][0]) + abs(person[i][1] - stairs[0][1])  # 사람 i -> 계단 0
        dis[i][1] = abs(person[i][0] - stairs[1][0]) + abs(person[i][1] - stairs[1][1])  # 사람 i -> 계단 0
    minT = 100000000000
    for k in range(1 << len(person)):