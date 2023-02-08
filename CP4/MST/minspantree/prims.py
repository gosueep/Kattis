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
        heapq.heappush(heap, (w, (first, dest)))

    print(heap)

    mst = set()
    mst_length = 0
    while len(mst) < N-1 and heap:
        src, dest = heapq.heappop(heap)



    if len(mst) != N-1:
        print('Impossible')
    else:
        print(mst_length)
        for v in sorted(mst):
            print(v[0], v[1])