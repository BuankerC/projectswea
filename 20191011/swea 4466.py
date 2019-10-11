'''
swea 4466. 최대 성적표 만들기 D3
'''

T = int(input())
for tc in range(1, T + 1):
    line = list(map(int, input().split()))
    n = line[0]
    k = line[1]
    score = list(map(int, input().split()))

    ans = 0
    for i in range(k):
        tmp = max(score)
        ans += tmp
        score.remove(tmp)

    print("#{} {}".format(tc, ans))