
if __name__ == '__main__':
    while True:
        N, M, Q = map(int, input().split())
        if [N, M, Q] == [0, 0, 0]:
            break

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


        for _ in range(Q):
            src, dest = map(int, input().split())

            if d[src][dest] == float('inf'):
                print('Impossible')
            else:
                print(d[src][dest])
        print()