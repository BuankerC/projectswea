'''
swea 1952 [모의 SW 역량테스트] 수영장
'''
for TC in range(1, int(input())+1):
    t = list(map(int, input().split()))
    p = list(map(int, input().split()))
    res = t[3]
    M = [0]*12
    DPM = t[1]/t[0]
    s = 0

    # 1. D와 M으로 배열 생성
    for i in range(len(p)):
        if p[i] > DPM:
            M[i] = t[1]
        else:
            M[i] = t[0]*p[i]

    # 2. 3개월 들이 들어선다.
    # 에러가 난 부분은 앞에서부터 3개월로 바꿔서 났을 거임
    # 아마도 3개월로 바꿀 때 어떤거를 바꿀지 계산해야 할듯,
    # 3개월 + 원소
    idx = 0
    while idx < 12:
        if idx < 10:
            if M[idx]+M[idx+1]+M[idx+2] > t[2]:
                M[idx], M[idx + 1], M[idx + 2] = t[2], 0, 0
                idx += 3
            else:
                idx += 1
        elif idx < 11:
            if M[idx] + M[idx + 1] > t[2]:
                M[idx], M[idx + 1] = t[2], 0
                idx += 2
            else:
                idx += 1
        elif idx < 12:
            if M[idx] > t[2]:
                M[idx] = t[2]
                idx += 1
            else:
                idx += 1
    s = sum(M)
    if s < res:
        res = s

    print("#{} {}".format(TC, res))