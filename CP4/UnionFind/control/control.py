import sys

sys.setrecursionlimit(2 ** 30)


class node:
    def __init__(self, p):
        self.parent = p
        self.size = 0


def union(a, b):
    a = nodes[find_set(a)]
    b = nodes[find_set(b)]
    if a != b:
        if a.size < b.size:
            a.parent = b.parent
            b.size += a.size
        else:
            b.parent = a.parent
            a.size += b.size


def find_set(v):
    if v == nodes[v].parent:
        return v
    nodes[v].parent = find_set(nodes[v].parent)
    return nodes[v].parent


N, Q = map(int, input().split())
nodes = [node(x+1) for x in range(N)]

for _ in range(Q):
    op, a, b = input().split()
    a = int(a)
    b = int(b)

    if op == '=':
        union(a, b)
    elif op == '?':
        print('yes') if find_set(a) == find_set(b) else print('no')

