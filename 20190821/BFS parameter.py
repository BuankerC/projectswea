def BFS(G, v):
    visited = [0]*n
    queue = []
    queue.append(v)
    while queue:
        t= queue.pop(0)
        if not visited[t]:
            visited[t] = True
            visit(t)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)