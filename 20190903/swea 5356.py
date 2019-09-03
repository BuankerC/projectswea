for T in range(int(input())):
    line = [list(input()) for _ in range(5)]
    big = max([len(st)] for st in line)
    for r in line:
        while len(r) < big:
            r.append('@')

    result = []
    for y in range(big):
        for x in range(len(line)):
            result.append(line[x][y])
    result = ''.join(result).replace('@','')
    print("#{} {}".format(T+1, result))