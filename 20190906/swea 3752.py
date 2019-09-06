'''
swea 3752 가능한 시험 점수 D4
'''

tc = int(input())
for t in range(1, tc+1):
    score = [0]
    vi = [0]*(100*100+1)
    n = input()
    nums = list(map(int, input().split()))
    for i in nums:
        for j in range(0, len(score)):
            tmp = i + score[j]
            if not vi[tmp]:
                vi[tmp] = True
                score.append(tmp)
    print('#{} {}'.format(t, len(score)))