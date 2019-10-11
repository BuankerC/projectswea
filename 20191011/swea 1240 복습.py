'''
swea 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 D3
'''

def is_valid(nums):
    result = 0
    sum_ = 0

    patterns = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9
    }
    last = nums.rindex('1')
    nums = nums[last - 55: last + 1]

    for i in range(8):
        n = patterns[nums[:7]]
        nums = nums[7:]
        sum_ += n

        if i == 7:
            result += n
        elif i % 2 == 0:
            result += n * 3
        else:
            result += n

    result = sum_ if result % 10 == 0 else 0

    return result

t = int(input())
ans = ''

for i in range(1, t + 1):
    n, m = map(int, input().split())

    codes = [input() for _ in range(n)]

    for code in codes:
        if code.count('1') >= 24:
            res = is_valid(code)
            break
    ans += "#{} {}\n".format(i, res)
print(ans)