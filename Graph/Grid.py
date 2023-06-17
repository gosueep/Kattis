from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())

    grid = []
    for i in range(n):
        row = [int(col) for col in input()]
        grid.append(row)

    q = deque([(0, (0, 0))])
    visited = set()

    shortest = float('inf')
    while q:
        distance, curr = q.pop()
        x, y = curr
        visited.add((x, y))

        if curr == (n-1, m-1):
            shortest = distance
            break

        k = grid[x][y]
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            dx *= k
            dy *= k
            if 0 <= x + dx < n and 0 <= y + dy < m and (x + dx, y + dy) not in visited:
                q.appendleft(((distance + 1), (x + dx, y + dy)))
                visited.add((x + dx, y + dy))


    if shortest == float('inf'):
        print(-1)
    else:
        print(shortest)

