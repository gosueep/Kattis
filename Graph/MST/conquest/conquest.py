
import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

if __name__ == "__main__":
    N, M = map(int, input().split())

    adjlist = defaultdict(list)
    for _ in range(M):
        src, dest = map(int, input().split())
        adjlist[src].append(dest)
        adjlist[dest].append(src)
    
    armies = [0] + [int(input()) for _ in range(N)]

    # Init heap
    first = 1
    heap = []
    for dest in adjlist[first]:
        heapq.heappush(heap, (armies[dest], dest))

    mst = set([first])   # stores seen nodes
    army = armies[first] # size of army
    while len(mst) < N and heap:
        w, dest = heapq.heappop(heap)
        
        if dest not in mst:
            if w < army:
                mst.add(dest)
                army += w
                for i in adjlist[dest]:
                    if i not in mst:
                        heapq.heappush(heap, (armies[i], i))

    print(army)
        