from collections import defaultdict, deque

if __name__ == '__main__':
    for _ in range(int(input())):
        numEnds = int(input())
        adjList = defaultdict(set)
        for _ in range(numEnds):
            endpoints = list(map(int, input().split()))
            if len(endpoints) == 2:
                adjList[endpoints[0]].add(endpoints[1])
                adjList[endpoints[1]].add(endpoints[0])
            else:
                adjList[endpoints[0]] = set()

        # print(adjList)

        visited = set()
        components = 0
        for node in adjList:
            # do bfs
            if node not in visited:
                bfs = deque([node])
                # bfs.append(node)
                while bfs:
                    curr = bfs.pop()
                    visited.add(curr)
                    for neighbor in adjList[curr]:
                        if neighbor not in visited:
                            bfs.append(neighbor)

                components += 1

        print(components-1)
