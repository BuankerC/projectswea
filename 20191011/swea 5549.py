'''
swea 5549. 홀수일까 짝수일까 D3
'''

tc = int(input())
for t in range(1, tc + 1):
    n = int(input())

    if n & 1 == 1:
        print('#%d Odd' % (t))
    else:
        print('#%d Even' % (t))