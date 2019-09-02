for t in range(int(input())):
    N, M = map(int, input().split())
    sample = []
    for i in range(M):
        temp_sample = list(map(int, input().split()))
        number = temp_sample[0]
        for index, value in enumerate(sample):
            if number < value:
                sample = sample[:index] + temp_sample + sample[index:]
                break
        else:
            sample += temp_sample
        if len(sample) > 10:
            sample = list(set(sample[:-10])) + sample[-10:]
    ans = []
    print(f"#{t+1} {' '.join([str(i) for i in sample[-1:-11:-1]])}")