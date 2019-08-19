def fibo(n):
    global memo
    if n>=2 and memo[n]==0: # 아직 fibo(n)이 계산되지 않음경우
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n] # fibo(n)이 계산되어 있므면 리턴


N = 7
memo = [0]*(N+1)
memo[0] = 0
memo[1] = 1


print(fibo(N))
print()