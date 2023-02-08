import sys
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


while True:
    N, M = map(int, input().split())
    if [N, M] == [0, 0]:
        break

    edges = {}
    for _ in range(M):
        src, dest, w = map(int, input().split())
        edges[(src, dest)] = w

    s = sorted(edges, key=lambda x: edges[x], reverse=True)

    ufds = UnionFind(N)
    mst = set()
    mst_length = 0
    while s:
        src, dest = s.pop()
        if ufds.find_set(src) != ufds.find_set(dest):
            mst.add((src, dest))
            mst_length += edges[(src, dest)]
            ufds.union(src, dest)

    if ufds.numSets > 1:
        print('Impossible')
    else:
        print(mst_length)
        for v in sorted(mst):
            v = sorted(v)
            print(v[0], v[1])

