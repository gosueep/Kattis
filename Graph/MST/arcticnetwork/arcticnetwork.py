# This seems like classic MST

# Prims implementation

import heapq
import math
from collections import defaultdict

for case in range(int(input())):
    channels, N = map(int, input().split()) # channels, N = nodes
    outposts = [] 
    for i in range(N):
        x, y = map(float, input().split())
        outposts.append((x,y))
    
    heap = []
    i = 0
    for j in range(N):
        if j != i:
            w = abs(math.dist(outposts[i], outposts[j]))
            heapq.heappush(heap, (w, j, i))

    mst = set([0])      # Storing nodes, not edges
    mst_lengths = []
    while len(mst) < N and heap:
        w, dest, src = heapq.heappop(heap)
        
        if dest not in mst:
            # print(w, dest)
            mst.add(dest)
            mst_lengths.append((w, dest, src))
            
            i = dest
            for j in range(N):
                if j != i and j not in mst:
                    w = abs(math.dist(outposts[i], outposts[j]))
                    heapq.heappush(heap, (w, j, i))

    mst_lengths.sort(key=lambda x: x[0], reverse=True)
    print('{0:.2f}'.format(mst_lengths[channels-1][0]))