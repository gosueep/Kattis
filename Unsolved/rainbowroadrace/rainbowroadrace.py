from collections import defaultdict
N, M = map(int, input().split())

adj = defaultdict(list)
for _ in range(M):
    src, dest, w, color = input().split()
    src, dest, w = map(int, [src, dest, w])
    adj[src].append((dest, w))
    adj[dest].append((src, w))
    
    d = [[float('inf') for i in range(N)] for j in range(N)]

    weights = {}
    for _ in range(M):
        src, dest, weight = map(int, input().split())
        if (src, dest) in weights:
            weights[src, dest] = min(weights[src, dest], weight)
        else:
            weights[src, dest] = weight
        d[src][dest] = weights[src, dest]

    for node in range(N):
        d[node][node] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        