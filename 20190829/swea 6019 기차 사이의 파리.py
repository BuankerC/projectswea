for tc in range(int(input())):
    D, A, B, F = map(int, input().split())
    print("#{} {}".format(tc + 1, F * D / (A + B)))