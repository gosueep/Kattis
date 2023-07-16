import sys
sys.setrecursionlimit(2 ** 30)

# Without Path Compression
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

# With Path compression
class UnionFind:
    def __init__(self, N):
        self.p = [x for x in range(N)]          # parent list
        self.rank = []                          # Not implemented
        self.sizes = [1 for x in range(N)]
        self.N = N

    # join two sets
    def union(self, a, b):
        a = self.find_set(self.p[a])
        b = self.find_set(self.p[b])
        if a != b:
            if self.sizes[a] < self.sizes[b]:
                self.p[a] = self.p[b]
                self.sizes[b] += self.sizes[a]
            else:
                self.p[b] = self.p[a]
                self.sizes[a] += self.sizes[b]

    # Find set of given int v
    def find_set(self, v):
        if v == self.p[v]:
            return v
        self.p[v] = self.find_set(self.p[v])
        return self.p[v]