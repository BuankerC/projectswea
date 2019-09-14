def main():
    global ans

    tc = int(input())
    for t in range(1, tc+1):
        line = list(map(int, input().split()))
        n = line[0]
        k = line[1]
        nums = list(map(int, input().split()))


        ans = 0
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if i & (1 << j):
                    tmp.append(nums[j])

            if sum(tmp) == k:
                ans += 1

        print("#%d %d"%(t, ans))

if __name__ == '__main__':
    main()