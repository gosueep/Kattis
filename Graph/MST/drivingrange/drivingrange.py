# REDO IN CPP
# OR FIGURE OUT SPEED BOOST

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2 ** 30)


class UnionFind:
    def __init__(self, N):
        self.p = [x for x in range(N)]          # parent list
        self.numSets = N
        self.N = N

    # join two sets
    def union(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            self.p[a] = self.p[b]
            self.numSets -= 1

    # Find set of given int v
    def find_set(self, v):
        if v == self.p[v]:
            return v
        self.p[v] = self.find_set(self.p[v])
        return self.p[v]


N, M = map(int, input().split())

edges = []
for _ in range(M):
    src, dest, w = map(int, input().split())
    edges.append((src, dest, w))

s = sorted(edges, key=lambda x: x[2], reverse=True)

ufds = UnionFind(N)
mst = []
while len(mst) < N and s:
    src, dest, w = s.pop()
    if ufds.find_set(src) != ufds.find_set(dest):
        mst.append(w)
        ufds.union(src, dest)

if ufds.numSets > 1:
    print('IMPOSSIBLE')
else:
    print(max(mst))