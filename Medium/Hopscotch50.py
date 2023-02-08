import heapq

if __name__ == '__main__':
    n, k = map(int, input().split())

    nodes = [[] for x in range(k+1)]


    dists = {}
    unvisited = []


    grid = []
    for row in range(n):
        for col, tile in enumerate(list(map(int, input().split()))):
            nodes[tile].append((row, col))
            dists[(row, col)] = float('inf')

    for n in nodes[1]:
        dists[n] = 0
        heapq.heappush(unvisited, (0, n))

    # Start = non-existant node connecting to all 1-tiles with edge weights of 0
    #        ALT: just push all onto heap
    # Stop  = non-existant node connecting to all k-tiles with edge weights of 0

    for

    print(nodes)

