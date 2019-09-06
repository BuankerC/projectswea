'''
swea 5607 조합 D3
'''

p = 1234567891

def power(base, ex):
    if ex == 0:
        return 1
    elif ex == 1:
        return base
    res = power(base, ex//2) % p

    if (ex % 2 == 1):
        return res * res % p * power(base, 1) % p
    else:
        return res * res % p

def main():
    factMap = [0] * 1000001
    factMap[0] = 1
    for i in range(1, len(factMap)):
        factMap[i] = factMap[i-1] * i % p

    t = int(input())
    for i in range(t):
        tmp = input().split()
        N = int(tmp[0])
        R = int(tmp[1])
        res = factMap[N] * power(factMap[N-R] * factMap[R] % p, p-2) % p
        print('#' + str(i+1) + ' ' + str(res))

if __name__ == '__main__':
    main()