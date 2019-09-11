'''
swea 1240 [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 D3
'''

t = int(input())

pw = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7,
      '0110111': 8, '0001011': 9}

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    start = []

    chk = 0
    for i in range(n):
        start.append(str(input()))

    for i in range(n):
        for j in range(0, 7):
            if chk == 1 and len(crypto) == 8:
                break
            crypto = []
            chk = 0
            for k in range(0, (m // 7) * 7, 7):
                if start[i][j + k:j + k + 7] in pw.keys():
                    crypto.append(pw[start[i][j + k:j + k + 7]])
                    chk = 1
                if len(crypto) == 8:
                    break

    if len(crypto) == 8:
        if ((crypto[0] + crypto[2] + crypto[4] + crypto[6]) * 3 + crypto[1] + crypto[3] + crypto[5] + crypto[7]) % 10 == 0:
            print(f'#{tc} {sum(crypto)}')
        else:
            print(f'#{tc} 0')
    else:
        print(f'#{tc} 0')