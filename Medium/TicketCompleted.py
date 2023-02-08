import math
from collections import defaultdict, deque

if __name__ == '__main__':
    cities, rails = map(int, input().split())

    adjList = defaultdict(set)
    for _ in range(rails):
        start, end = map(int, input().split())

        adjList[start].add(end)
        adjList[end].add(start)

    components = []
    visited = set()
    for c in range(1, cities+1):
        if c not in visited:
            bfs = deque()
            bfs.append(c)
            visited.add(c)
            components.append(1)
            while bfs:
                curr = bfs.popleft()
                for n in adjList[curr]:
                    if n not in visited:
                        bfs.append(n)
                        visited.add(n)
                        components[-1] += 1

    totalRoutes = math.comb(cities, 2)
    availableRoutes = sum([math.comb(x, 2) for x in components])
    print(availableRoutes / totalRoutes)
