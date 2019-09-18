'''
swea 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 D3
'''

def quickSort(aList, l, r):
    global N
    if l < r:
        s = partition(aList, l, r)
        if s == N//2:
            return aList[s]
        elif s > N//2:
            quickSort(aList, l, s - 1)
        else:
            quickSort(aList, s+1, r)
    return aList[N//2]


def partition(aList, l, r):
    p = aList[l]
    i = l
    j = r
    while i < j:
        while aList[i] <= p and i < r:
            i += 1
        while aList[j] >= p and j > l:
            j -= 1
        if i < j:
            aList[i], aList[j] = aList[j], aList[i]
    aList[l], aList[j] = aList[j], aList[l]

    return j


for TC in range(1, int(input())+1):
    N = int(input())
    case = list(map(int, input().split()))
    print('#{} {}'.format(TC, quickSort(case, 0, len(case)-1)))