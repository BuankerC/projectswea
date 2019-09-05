'''
swea 4408 자기 방으로 돌아가기
'''

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    route = [0] * 200
    for _ in range(n):
        start, end = map(int, input().split())
        start, end = min(start, end), max(start,end)
        start, end = (start+1)//2-1, (end+1)//2-1

        for i in range(start, end+1):
            route[i] += 1
    max_route = 0
    for r in route:
        if r > max_route:
            max_route = r
    print('#{} {}'.format(tc, max_route))