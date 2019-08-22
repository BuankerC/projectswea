import sys

def find():
    maxI = 0
    for i in range(N):
        num = int(v[i])
        card[num] = card[num] + 1
        if card[maxI] < card[num]: # 개수가 더 많은 숫자 카드 찾기
            maxI = num
        else:
            if card[maxI] == card[num]: # 개수가 같은 경우 더 큰 숫자 카드 찾기
                maxI = max(maxI, num)
    return maxI

sys.stdin = open('input.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    v = input()
    card = [0] * 10

    m = find()
    print('#{} {} {}'.format(tc, m, card[m]))