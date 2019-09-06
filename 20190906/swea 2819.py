'''
swea 2819 격자판의 숫자 이어붙이기 D4
'''

def goto(root_map, vi, x, y, depth, go, num):
    if depth == 6:
        vi.append(num)
        return

    if go == 'u':
        if x - 1 < 0:
            return
        else:
            num += root_map[x-1][y]
            x -= 1
            depth += 1
    elif go == 'd':
        if x + 1 > 3:
            return
        else:
            num += root_map[x+1][y]
            x += 1
            depth += 1
    elif go == 'r':
        if y + 1 > 3:
            return
        else:
            num += root_map[x][y+1]
            y += 1
            depth += 1
    elif go == 'l':
        if y - 1 < 0:
            return
        else:
            num += root_map[x][y-1]
            y -= 1
            depth += 1

    goto(root_map, vi, x, y, depth, 'u', num)
    goto(root_map, vi, x, y, depth, 'd', num)
    goto(root_map, vi, x, y, depth, 'r', num)
    goto(root_map, vi, x, y, depth, 'l', num)


def main():
    test_case = int(input())

    for t in range(0, test_case):
        vi = []
        root_map = [[0]*4 for i in range(4)]
        for i in range(0, 4):
            line = input().split()
            for j in range(0, 4):
                root_map[i][j] = line[j]

        for i in range(0, 4):
            for j in range(0, 4):
                goto(root_map, vi, i, j, 0, None, root_map[i][j])

        vi = set(vi)
        print("#" + str(t+1) + " " + str(len(vi)))


if __name__ == '__main__':
    main()