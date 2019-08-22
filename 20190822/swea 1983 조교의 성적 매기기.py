T = int(input())

for case in range(1, T + 1):
    firstInput = list(map(int, input().split()))
    students = firstInput[0]
    pergrade = students // 10
    target = firstInput[1]
    point = [0] * students
    grade = [0] * students
    gradeslist = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for num in range(students):
        point[num] = list(map(int, input().split()))
        point[num] = (point[num][0] * 35 + point[num][1] * 45 + point[num][2] * 20, num + 1)

    # 정렬 구현해보기
    point.sort()
    point.reverse()

    for num in range(10):
        targetgrade = gradeslist[num]
        for i in range(num * pergrade, (num + 1) * pergrade):
            grade[i] = targetgrade

    for info in range(len(point)):
        if point[info][1] == target:
            print(f'#{case} {grade[info]}')
            break