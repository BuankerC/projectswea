'''
swea 4013. [모의 SW 역량테스트] 특이한 자석
'''

class Magnet:
    def __init__(self, mag_id, gear):
        self.mag_id = mag_id
        self.gear = gear
        self.top = 0

    def turn(self, direction):
        self.top = (self.top - direction) % 8

    def get_left(self):
        return self.gear[(self.top - 2) % 8]

    def get_right(self):
        return self.gear[(self.top + 2) % 8]

def calculate_score(ms):
    score = 0
    for m in ms:
        score += int(m.gear[m.top]) * (2 ** m.mag_id)
    return score

for tc in range(1, int(input()) + 1):
    K = int(input())
    ms = []
    for i in range(4):
        ms.append(Magnet(i, list(input().split())))
    turns = []
    for _ in range(K):
        turns.append(list(map(int, input().split())))
        turns[-1][0] -= 1
    for turn in turns:
        check = [0, 0, 0, 0]
        check[turn[0]] = turn[1]
        for i in range(turn[0], 0, -1):
            if ms[i].get_left() != ms[i - 1].get_right():
                check[i - 1] = -1 * check[i]
        for i in range(turn[0], 3):
            if ms[i].get_right() != ms[i + 1].get_left():
                check[i + 1] = -1 * check[i]
        for i in range(4):
            ms[i].turn(check[i])
    print('#{} {}'.format(tc, calculate_score(ms)))