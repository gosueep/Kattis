# This seems like classic MST

# Prims implementation

import heapq
import math
from collections import defaultdict

for case in range(int(input())):
    N = int(input())
    islands = [] 
    for i in range(N):
        x, y = map(float, input().split())
        islands.append((x,y))
    
    heap = []
    i = 0
    for j in range(N):
        if j != i:
            w = abs(math.dist(islands[i], islands[j]))
            heapq.heappush(heap, (w, j))

    mst = set([0])      # Storing nodes, not edges
    mst_length = 0
    while len(mst) < N and heap:
        w, dest = heapq.heappop(heap)
        
        if dest not in mst:
            # print(w, dest)
            mst.add(dest)
            mst_length += w
            
            i = dest
            for j in range(N):
                if j != i and j not in mst:
                    w = abs(math.dist(islands[i], islands[j]))
                    heapq.heappush(heap, (w, j))

    print(mst_length) 