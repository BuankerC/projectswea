T = int(input())
result = []
for t in range(1, T+1):
    a = sum(map(int, input().split()))
    result.append(f"#{t} {a}")
print("\n".join(result))