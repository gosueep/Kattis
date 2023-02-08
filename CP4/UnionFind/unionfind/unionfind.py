import sys

sys.setrecursionlimit(2 ** 30)


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


N, Q = map(int, input().split())
ufds = UnionFind(N)

for _ in range(Q):
    op, a, b = input().split()
    a = int(a)
    b = int(b)

    if op == '=':
        ufds.union(a, b)
    elif op == '?':
        print('yes') if ufds.find_set(a) == ufds.find_set(b) else print('no')

