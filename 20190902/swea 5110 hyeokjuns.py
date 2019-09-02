class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self.length = 0

        if iterable:
            for value in iterable:
                self.push(value)

    def push(self, value):

        node = Node(value)

        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        self.length += 1

        return self

    def find(self, node):
        value = node.value
        target_node = self.head

        for i in range(self.length):
            if target_node.value > value:
                return target_node

            target_node = target_node.next

        return None

    def link_sequence(self, DLL):

        target_node = self.find(DLL.head)

        if target_node:
            prev_node = target_node.prev

            # 중간에 삽입 -> 헤드, 테일 변경 없음
            if prev_node:
                prev_node.next = DLL.head
                DLL.head.prev = prev_node
                DLL.tail.next = target_node
                target_node.prev = DLL.tail

            # 맨앞에 삽입 -> 헤드 변경 필요
            else:
                DLL.tail.next = target_node
                target_node.prev = DLL.tail
                self.head = DLL.head

        # 맨 뒤에 삽입 -> 테일 변경 필요
        else:
            self.tail.next = DLL.head
            DLL.head.prev = self.tail
            self.tail = DLL.tail

        self.length += DLL.length

    def get_data(self):
        data = []

        current = self.head
        for _ in range(self.length):
            data.append(current.value)
            current = current.next

        return data

    def get_data_reverse_10(self):
        data = []

        current = self.tail

        for i in range(10):
            data.append(current.value)
            current = current.prev

        return data


# 테스트케이스 전체 통과 => 짧은 리스트는 오히려 더 오래 걸리는 편인데, 길어지면 능력을 발휘하는듯
def process_with_dll(tc, M):
    DLL = DoublyLinkedList(list(map(int, input().split())))

    for _ in range(M - 1):
        next_dll = DoublyLinkedList(list(map(int, input().split())))
        DLL.link_sequence(next_dll)

    print("#{} {}".format(tc, ' '.join(map(str, DLL.get_data_reverse_10()))))

import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    process_with_dll(tc, M)
