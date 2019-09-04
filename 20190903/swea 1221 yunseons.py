ref = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
for t in range(int(input())):
    trash, n = input().split()
    print(trash)
    N = int(n)
    strings = list(input().split())
    nums = [ref[string] for string in strings]
    nums.sort()
    for i in nums:
        for key, val in ref.items():
            if val == i:
                print(key, end=' ')
    print()