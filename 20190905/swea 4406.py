'''
swea 4406 모음이 보이지 않는 사람 D3
'''
T = int(input())
for tc in range(1, T+1):
    check = ['a', 'e', 'i', 'o', 'u']
    s = list(input())
    for c in check:
        while c in s:
            s.remove(c)
    print('#'+str(tc),''.join(s))