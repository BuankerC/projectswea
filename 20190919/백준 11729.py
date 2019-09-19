'''
백준 11729 하노이 탑 이동 순서
'''

def hanoi(disk, start, mid, end):
    if disk == 1:
        print(start, end)
    else:
        hanoi(disk - 1, start, end, mid)
        print(start, end)
        hanoi(disk - 1, mid, start, end)

total_disk = int(input())
total_move = 0

for disk in range(total_disk):
    total_move *= 2
    total_move += 1

print(total_move)
hanoi(total_disk, 1, 2, 3)