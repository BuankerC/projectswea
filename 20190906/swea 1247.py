'''
swea 1247 최적 경로 D5
'''

ans = 999999

# last_x, y는 직전 방문 좌표.
def backtrack(customers, visited, idx, last_x, last_y, home_x, home_y, distance):
    global ans
    if idx == len(customers):
        # 마지막 고객 방문 끝, 집까지의 거리를 더함
        ndist = abs(last_x - home_x) + abs(last_y - home_y)
        distance += ndist
        if ans > distance:
            ans = distance
        return

    for i in range(0, len(customers)):
        if not visited[i]:
            if ans < distance:
                return

            visited[i] = True
            ndist = abs(last_x - customers[i][0]) + abs(last_y - customers[i][1])
            backtrack(customers, visited, idx+1, customers[i][0], customers[i][1], home_x, home_y, distance + ndist)
            visited[i] = False


def main():
    test_case = int(input())
    for t in range(0, test_case):
        global ans
        num = int(input())
        line = input().split()
        dot = [[0] * 2 for i in range(num+2)]
        j = 0

        for i in range(0, num+2):
            dot[i][0] = int(line[j])
            dot[i][1] = int(line[j+1])
            j += 2

        visited = [False]*num

        work = dot[0]
        home = dot[1]
        dot = dot[2:]
        ans = 99999
        backtrack(dot, visited, 0, work[0], work[1], home[0], home[1], 0)
        print("#" + str(t+1) + " " + str(ans))
        ans = 0

if __name__ == '__main__':
    main()
