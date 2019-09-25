input()
a = list(map(int, input().split()))
count = 0

def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i*i <= x:
        if x % i == 0:
            return False
        i += 1

    return True

for i in a:
    if is_prime(i):
        count += 1

print(count)