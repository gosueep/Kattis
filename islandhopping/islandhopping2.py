# Kruskal's

import math
import sys
import heapq
sys.setrecursionlimit(2 ** 30)


class UnionFind:
    def __init__(self, N):
        self.p = [x for x in range(N)]          # parent list
        # self.rank = []                          # Not implemented
        # self.sizes = [1 for x in range(N)]    # Not needed?
        self.numSets = N
        self.N = N

    # join two sets
    def union(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
        #     if self.sizes[a] < self.sizes[b]:
        #         self.p[a] = self.p[b]
        #         self.sizes[b] += self.sizes[a]
        #     else:
        #         self.p[b] = self.p[a]
        #         self.sizes[a] += self.sizes[b]
            self.p[a] = self.p[b]
            self.numSets -= 1

    # Find set of given int v
    def find_set(self, v):
        if v == self.p[v]:
            return v
        self.p[v] = self.find_set(self.p[v])
        return self.p[v]


for case in range(int(input())):
    N = int(input())
    islands = [] 
    for i in range(N):
        x, y = map(float, input().split())
        islands.append((x,y))
        
    edges = []
    for i in range(N):
        for j in range(i+1,N):
            w = abs(math.dist(islands[i], islands[j]))
            edges.append((w, i, j)) 

    heapq.heapify(edges)
    i = 0

    ufds = UnionFind(N)
    mst = set()
    mst_length = 0
    while len(mst) < N-1:
        w, src, dest = heapq.heappop(edges)
        if ufds.find_set(src) != ufds.find_set(dest):
            mst.add((src, dest))
            mst_length += w
            ufds.union(src, dest)
        i += 1

    print(mst_length)

