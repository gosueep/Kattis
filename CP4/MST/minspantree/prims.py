import heapq
from collections import defaultdict

while True:
    N, M = map(int, input().split())
    if [N, M] == [0, 0]:
        break
    if M == 0:
        print('Impossible')
        continue

    adjlist = defaultdict(list)
    for _ in range(M):
        src, dest, w = map(int, input().split())
        adjlist[src].append((dest, w))
        adjlist[dest].append((src, w))


    # Get arbitrary element with edges - ONLY NEED IF GRAPH IS NOT CONNECTED
    first = 0
    while not adjlist[first]:
        first += 1

    # Init heap
    heap = []
    for dest, w in adjlist[first]:
        heapq.heappush(heap, (w, first, dest))

    mst = set([first])  # stores seen nodes
    edges = []
    mst_length = 0
    while len(mst) < N and heap:
        w, src, dest = heapq.heappop(heap)
        
        if dest not in mst:
            mst.add(dest)
            mst_length += w
            edges.append(sorted((src, dest)))
            for i, w in adjlist[dest]:
                if i not in mst:
                    heapq.heappush(heap, (w, dest, i))

    if len(mst) != N:
        print('Impossible')
    else:
        print(mst_length)
        for x, y in sorted(edges):
            print(x, y)