'''
swea 5177 이진 힙 D2
'''

class Minheap:
    def __init__(self, N):
        self.heap = [0] * (N+1)
        self.size = 0

    def perce_up(self, i):
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i // 2], self.heap[i] = self.heap[i], self.heap[i // 2]
            i //= 2

    def insert(self, n):
        self.heap[self.size + 1] = n
        self.size += 1
        self.perce_up(self.size)

    def sum_of_pres(self):
        cnt = 0
        i = self.size
        while i // 2 > 0:
            cnt += self.heap[i // 2]
            i //= 2
        return cnt

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    heap = Minheap(N)
    nums = [int(n) for n in input().split()]
    for n in nums:
        heap.insert(n)
    print('#%d %d' % (t, heap.sum_of_pres()))