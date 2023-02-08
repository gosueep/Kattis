from collections import deque

if __name__ == '__main__':
    r, c = map(int, input().split())

    grid = []
    for i in range(r):
        grid.append([int(x) for x in input()])

    visited = set()
    graphs = [[0 for x in range(c)] for y in range(r)]
    graphID = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] != -1:
            # if (i, j) not in visited:
                currSearch = deque()
                currSearch.append((i, j))
                graphs[i][j] = (graphID, grid[i][j])
                while currSearch:
                    rC, cC = currSearch.pop()
                    # visited.add((rC, cC))

                    for newR, newC in [(rC + 1, cC), (rC, cC + 1), (rC - 1, cC), (rC, cC - 1)]:
                        # (newR, newC) not in visited
                        if 0 <= newR < r and 0 <= newC < c and grid[newR][newC] != -1 and grid[rC][cC] == grid[newR][newC]:
                            currSearch.append((newR, newC))
                            graphs[newR][newC] = (graphID, grid[newR][newC])
                    grid[rC][cC] = -1
                graphID += 1

    for query in range(int(input())):
        r1, c1, r2, c2 = map(int, input().split())
        if graphs[r1-1][c1-1][0] == graphs[r2-1][c2-1][0]:
            print('binary') if graphs[r1-1][c1-1][1] == 0 else print('decimal')
        else:
            print('neither')

