import math
from collections import defaultdict
import heapq


def djikstra(adjList, src):
    dists = {}
    unvisited = []

    for node in adjList:
        dists[node] = math.inf
    dists[src] = 0


    for _ in range(len(adjList)):
        for node in adjList:
            if dists[node] != math.inf:
                for dest, weight in adjList[node]:
                    dists[dest] = min(dists[node], dists[src] + weight)

    # Negative cycle check
    for node in adjList:
        if dists[node] != math.inf:
            for dest, weight in adjList[node]:
                if dists[dest] > dists[node] + weight:
                    return False

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

        shortestPaths = djikstra(adjList, startNode)

        for _ in range(numQueries):
            dest = int(input())
            
            if dest not in shortestPaths or shortestPaths[dest] == math.inf:
                print("Impossible")
            else:
                print(shortestPaths[dest])
        print()

        inputLine = input()
