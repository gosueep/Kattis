import math
from collections import defaultdict
import heapq


def dijkstra(adjList, src):
    dists = {}
    unvisited = []

    for node in adjList:
        dists[node] = math.inf
    dists[src] = 0
    heapq.heappush(unvisited, (0, src))

    while unvisited:
        curr = heapq.heappop(unvisited)
        curr = curr[1]

        for neighbor, weight in adjList[curr]:
            altDist = dists[curr] + weight
            if altDist < dists[neighbor]:
                dists[neighbor] = altDist
                heapq.heappush(unvisited, (altDist, neighbor))

    return dists


if __name__ == '__main__':

    inputLine = input()

    while inputLine != "0 0 0 0":

        numNodes, numEdges, numQueries, startNode = map(int, inputLine.split())

        adjList = defaultdict(list)
        for _ in range(numEdges):
            src, dest, weight = map(int, input().split())

            adjList[src].append([dest, weight])
            if dest not in adjList:
                adjList[dest] = []

        shortestPaths = dijkstra(adjList, startNode)

        for _ in range(numQueries):
            dest = int(input())
            if dest not in shortestPaths or shortestPaths[dest] == math.inf:
                print("Impossible")
            else:
                print(shortestPaths[dest])
        print()

        inputLine = input()
