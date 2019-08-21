q = [0]*10 # 10칸짜리 큐 생성
front = -1
rear = -1

rear += 1
q[rear] = 1 # enqueue(1)

rear += 1
q[rear] = 2 # enqueue(2)

rear += 1
q[rear] = 3 # enqueue(3)

while ( front != rear ): # q_is_not_empty
    front += 1
    print(q[front])