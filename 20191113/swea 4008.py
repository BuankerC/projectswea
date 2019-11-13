'''
swea 4008 [모의 SW 역량테스트] 숫자 만들기
'''

def Operation(N, cnt, res):
    global operator, numbers, min_value, max_value
    if cnt == N:
        if res < min_value:
            min_value = res
        if res > max_value:
            max_value = res
        return

    if operator[0]:
        operator[0] -= 1
        Operation(N, cnt + 1, res + numbers[cnt])
        operator[0] += 1

    if operator[1]:
        operator[1] -= 1
        Operation(N, cnt + 1, res - numbers[cnt])
        operator[1] += 1

    if operator[2]:
        operator[2] -= 1
        Operation(N, cnt + 1, res * numbers[cnt])
        operator[2] += 1

    if operator[3]:
        operator[3] -= 1
        Operation(N, cnt + 1, int(res / numbers[cnt]))
        operator[3] += 1

for tc in range(int(input())):
    N = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_value, max_value = 0xffffffff, -10e9

    Operation(N, 1, numbers[0])

    print('#{} {}'.format(tc + 1, max_value - min_value))