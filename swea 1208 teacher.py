for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    while(dump > 0):
        maxIdx = 0;
        minIdx = 0;
        for i in range(1, 100):
            if(box[maxIdx] < box[i]):
                maxIdx = i
            if(box[minIdx] < box[i]):
                minIdx = i
            diff = box[maxIdx] - box[minIdx]
            if (diff <= 1):
                break
            else:
                box[maxIdx] = box[maxIdx] - 1
                box[minIdx] = box[minIdx] + 1
        dump = dump -1
    print()