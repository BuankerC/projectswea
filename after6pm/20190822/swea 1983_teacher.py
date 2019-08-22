grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    score = []
    for i in range(N):
        mid, fin, hw = map(int, input().split())
        score.append(mid*0.35 + fin*0.45 + hw*0.2)
    c = 0

    for i in range(N):
        if(score[K-1] < score[i]):
            c += 1
    print('#', end='')
    print(tc, end = '')
    print(grade[c//N//10])