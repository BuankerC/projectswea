import math
for s in range(1, int(input())+1):
    score_list = list(map(int, input().split()))
    n = score_list[0]
    k = score_list[1]
    grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade_list = []
    for i in range(1, n+1):
        score = list(map(int, input().split()))
        grade_list.append(score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2)
    j = n - 1
    for grade_check in grade_list:
        if grade_list[k-1] > grade_check:
            j -= 1
    i = math.floor(j/(n/10))
    print(f'#{s} {grade[i]}')