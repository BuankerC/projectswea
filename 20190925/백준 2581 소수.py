def f(n):
    if n == 1: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

a = int(input())
b = int(input())
d = [i for i in range(a, b + 1) if f(i)]
if len(d) == 0:
    print(-1)
else:
    print(sum(d))
    print(min(d))