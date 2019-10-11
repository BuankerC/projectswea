'''
swea 5356. 의석이의 세로로 말해요 D3
'''

tc = int(input())
for t in range(1, tc+1):
    m = [['-']*15 for _ in range(5)]
    for i in range(5):
        line = input()
        for j in range(len(line)):
            m[i][j] = line[j]


    print("#%d "%t, end='')
    for i in range(15):
        for j in range(5):
            if m[j][i] != '-':
                print(m[j][i], end='')
    print()