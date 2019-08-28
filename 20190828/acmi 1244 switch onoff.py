N = int(input())
sw = [0] + list(map(int, input().split())) # 스위치는 1번부터
M = int(input())
for i in range(M):
    s, c = map(int, input().split())
    if s == 1:  # 남학생일 때
        for j in range(1, N + 1):
            # if j % c == 0:
            if sw[i] == 0:
                sw[i] = 1
            else:
                sw[i] = 0
            # => sw[i] = (sw[i]+1) % 2
            # => sw[i] = 1 if sw[i]==0 else 0
        # j = 1
        # while(j * c <= N):
        #     sw[j * c] =sw([j * c] + 1) % 2
        #     j += 1
    else: # 여학생일 때, 스위치 번호를 중심으로 대칭인 구간을 반전
        sw[c] = (sw[c]+1) % 2  # 지정번호를 반전
        left = c - 1
        right = c + 1
        # 스위치 번호가 유효하고, 양 옆의 스위치 상태가 같으면
        while(left >= 1 and right <= N and sw[left] == sw[right]):
            sw[left] = (sw[left] + 1) % 2
            sw[right] = (sw[right] + 1) % 2
            left -= 1
            right += 1
        k = 1 # 스위치 개수로 관리하는 경우
        while(c-k >=1 and c+k <= N and sw[c-k] == sw[c+k]):
            sw[c-k]
            sw[c+k]
            k += 1
for i in range(1, N + 1):
    print('{}'.format(sw[i]), end = ' ')
    if(i % 20 == 0):
        print()