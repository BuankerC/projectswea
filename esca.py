import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    s = 0
    for i in range(0, 10):
        if(arr[i]%2 != 0):
            s = s + arr[i]

    print('#{} {}'.format(tc, s))
