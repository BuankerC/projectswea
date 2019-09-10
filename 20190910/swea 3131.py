def main():
    prime_map = []
    n = 1000000
    a = [False, False] + [True] * (n - 1)

    for i in range(2, n + 1):
        if a[i]:
            prime_map.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False

    for i in prime_map:
        print(str(i)+" ", end='')

if __name__ == '__main__':
    main()