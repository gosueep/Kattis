from functools import reduce

def convex_hull_graham(points):
    TURN_LEFT, TURN_RIGHT, TURN_NONE = (1, -1, 0)

    def cmp(a, b):
        return (a > b) - (a < b)

    def turn(p, q, r):
        return cmp((q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1]), 0)

    def _keep_left(hull, r):
        while len(hull) > 1 and turn(hull[-2], hull[-1], r) != TURN_LEFT:
            hull.pop()
        if not len(hull) or hull[-1] != r:
            hull.append(r)
        return hull

    points = sorted(points)
    l = reduce(_keep_left, points, [])
    u = reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l


while True:
    N = int(input())

    if N == 0:
        break

    startX, startY = 10e6, 10e6
    points = []
    for i in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
        if x <= startX and y <= startY:
            startX, startY = x, y
    
    p = convex_hull_graham(points)
    print(len(p))
    for x,y in p:
        print(x, y)