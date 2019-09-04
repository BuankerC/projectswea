'''
swea 1493 수의 새로운 연산 D3
'''

N = 300
fact = [0] * (N + 1)
fact[0] = 0
fact[1] = 1
for i in range(2, N + 1):
    fact[i] = fact[i-1] + i-1

def get_xy(n):
    for i in range(len(fact)):
        if fact[i] > n:
            tmp = i-1
            break
    k = tmp - (n - fact[tmp])
    return tmp+1-k, k

def get_val(xy):
    idx = xy[0] + xy[1] - 1
    return fact[idx] + idx - xy[1]

T = int(input())
for tc in range(1, T+1):
    u, v = map(int, input().split())
    tmp_u = get_xy(u)
    tmp_v = get_xy(v)

    print('#{} {}'.format(tc, get_val([tmp_u[0] + tmp_v[0], tmp_u[1] + tmp_v[1]])))