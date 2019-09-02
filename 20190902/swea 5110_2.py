class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cur = self.tail

    def insert(self, item):
        newNode = Node(item)
        newNode.prev = self.cur.prev
        newNode.next = self.cur
        self.cur.prev.next = newNode
        self.cur.prev = newNode

    def moveToBigger(self, item):
        self.cur = self.head.next
        while self.cur.data != None:
            if self.cur.data > item:
                break
            self.cur = self.cur.next

tc = int(input())
for t in range(1, tc+1):
    N, M = map(int, input().split())
    res = DoublyLinkedList()
    for num in nums:
        res.insert(num)

    for _ in range(M-1):
        nums = [int(n) for n in input().split()]
        res.moveToBigger(nums[0])
        for num in nums:
            res.insert(num)

    print(f'#{t}', end=' ')
    i = 0
    p = res.tail
    while i < 9:
        print(p.prev.data, end=' ')
        p = p.prev
        i += 1
    print(p.data)