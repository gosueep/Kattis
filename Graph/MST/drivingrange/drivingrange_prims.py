
import sys
input = sys.stdin.readline
import heapq
from collections import defaultdict

if __name__ == "__main__":
    N, M = map(int, input().split())

    adjlist = defaultdict(list)
    for _ in range(M):
        src, dest, w = map(int, input().split())
        adjlist[src].append((dest, w))
        adjlist[dest].append((src, w))

    # Init heap
    first = 0
    heap = []
    for dest, w in adjlist[first]:
        heapq.heappush(heap, (w, first, dest))

    mst = set([first])  # stores seen nodes
    while len(mst) < N and heap:
        old_w, _, dest = heapq.heappop(heap)
        
        if dest not in mst:
            mst.add(dest)
            for i, w in adjlist[dest]:
                if i not in mst:
                    heapq.heappush(heap, (w, dest, i))

    if len(mst) != N:
        print('IMPOSSIBLE')
    else:
        print(old_w)