def find(n, k):
    cnt = 0
    q = []
    v = [0] * (k + 1)
    q.append(n)
    v[n] = 1
    while(len(q) > 0):
        n = q.pop(0)
        cnt += 1
        for i in range(2, k+1):
            if(adj[n][i] == 1 and v[i] == 0 and v[n] <= 2):
                q.append(1)
                v[i] = v[n] + 1
    return (cnt - 1)