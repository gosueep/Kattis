from collections import defaultdict, deque

if __name__ == '__main__':
    for _ in range(int(input())):
        numEnds = int(input())
        numRoads = int(input())
        adjList = [set() for x in range(numEnds)]
        for _ in range(numRoads):
            src, dest = map(int, input().split())
            adjList[src].add(dest)
            adjList[dest].add(src)

        visited = set()
        components = 0
        for node in range(numEnds):
            # do bfs
            if node not in visited:
                bfs = deque([node])
                # bfs.append(node)
                while bfs:
                    curr = bfs.popleft()
                    visited.add(curr)
                    for neighbor in adjList[curr]:
                        if neighbor not in visited:
                            bfs.append(neighbor)

                components += 1

        print(components-1)
