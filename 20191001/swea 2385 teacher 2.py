def find(k, pcnt):
    if k & (i << 1) == 0:
        t0[dis[i][0] + 1] += 1
    else:
        t1[dis[i][1] + 1] += 1
    #시간별 계단에 있는 인원
    sta0 = [0] * 200
    sta1 = [0] * 200
    last0 = 0  # 마지막 사람이 계단을 통과한 시간
    last1 = 0  # 마지막 사람이 계단을 통과한 시간
    for i in range(99):
        if (t0[i] != 0):  # 0번 입구에 도착 인원이 있으면
            if (sta0[i] + t0[i] > 3):  # 초과 인원은 다음 시간으로 넘김
                rest = sta0[i] + t0[i] - 3
                t1[i + 1] += rest
                t1[i] -= rest
            j = 0
            while (j < )

