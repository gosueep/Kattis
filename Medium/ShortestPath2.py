import heapq
import math
from collections import defaultdict


def djikstra2(adjList, src):
    dists = {}
    unvisited = []

    for node in adjList:
        dists[node] = math.inf
    dists[src] = 0
    heapq.heappush(unvisited, (0, src))

    while unvisited:
        curr = heapq.heappop(unvisited)
        curr = curr[1]

        for neighbor, t_0, P, time in adjList[curr]:

            altDist = dists[curr] + time

            if dists[curr] <= t_0:
                altDist += t_0 - dists[curr]
            else:
                if P == 0:
                    continue
                else:
                    wait = P - ((dists[curr] - t_0) % P)
                    if wait != P:                                   # if wait = full time of interval, no wait needed
                        altDist += wait


            if altDist < dists[neighbor]:
                dists[neighbor] = altDist
                heapq.heappush(unvisited, (altDist, neighbor))

    return dists


if __name__ == '__main__':
    while True:
        numNodes, numEdges, numQueries, startNode = map(int, input().split())

        if numNodes == 0:
            break

        adjList = defaultdict(list)
        for _ in range(numEdges):
            src, dest, t_0, P, weight = map(int, input().split())

            adjList[src].append([dest, t_0, P, weight])
            if dest not in adjList:
                adjList[dest] = []

        shortestPaths = djikstra2(adjList, startNode)

        for _ in range(numQueries):
            dest = int(input())
            if dest not in shortestPaths or shortestPaths[dest] == math.inf:
                print("Impossible")
            else:
                print(shortestPaths[dest])
        print()
