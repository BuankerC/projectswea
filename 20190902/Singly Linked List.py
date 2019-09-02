import sys


class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link


def addLast(data):  # 마지막 노드 추가
    global pHead
    if pHead == None:
        pHead = Node(data, None)
    else:
        p = pHead
        while p.link != None:
            p = p.link
        p.link = Node(data, None)
    return


def add(data, idx):  # idx 위치에 새 노드 추가
    global pHead
    p = pHead
    n = 0
    while n < idx - 1:
        p = p.link
        n += 1
    t = p.link
    p.link = Node(data, t)
    return


def get(idx):  # idx의 데이터 리턴