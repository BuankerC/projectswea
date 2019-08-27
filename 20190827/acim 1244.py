N = int(input())
sw = [0] + list(map(int, input().split())) # 스위치는 1번부터
M = int(input())
for i in range(M):
    s, c = map(int, input().split())
    if s == 1: # 남학생
        for i in range(1, N+1):
            if i%c == 0: # 스위치 번호가 c의 배수면 반전
                sw[i] = (sw[i]+1) % 2
    else: # 여학생
        left = c - 1
        right = c + 1
        sw[c] = (sw[c] + 1) % 2
        while(left > 0 and right <= M and)