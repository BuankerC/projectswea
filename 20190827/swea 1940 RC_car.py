test_case = int(input())
for i in range(test_case):
    command = int(input())
    distance = 0
    speed = 0
    for num in range(command):
        velocity = [int(v) for v in input().split()]
        if velocity[0] == 1:
            speed += velocity[1]
        elif velocity[0] == 2:
            speed -= velocity[1]

        if speed > 0:
            distance += speed
        else:
            speed = 0
            distance += speed
    print('#' + str(i + 1), distance)