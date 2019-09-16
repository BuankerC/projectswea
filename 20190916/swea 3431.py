'''
swea 3431 준환이의 운동관리 D3
'''

tc = int(input())
for t in range(1, tc + 1):
    line = list(map(int, input().split()))
    print('#'+str(t)+" ", end='')
    if line[2] in range(line[0], line[1] + 1):
        print("0", end='')
    elif line[2] < line[0]:
        print(line[0] - line[2], end='')
    elif line[1] < line[2]:
        print("-1", end='')
    print()