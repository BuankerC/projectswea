t = int(input())
for tc in range(t):
    p, q, r, s, w = map(int, input().split())

    a = w * p

    if w < r:
        result = q
    else:
        result = q + (w - r) * s

    if a > result:
        final = result
    else:
        final = a
    print(f'#{tc+1} {final}')