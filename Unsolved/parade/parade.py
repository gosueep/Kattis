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


N = int(input())
nazis = [tuple(map(int, input().split())) for _ in range(N)]

S = int(input())
soviets = [tuple(map(int, input().split())) for _ in range(S)]

# print(nazis, soviets)
# print(convex_hull_graham(nazis))

conhull = convex_hull_graham(nazis)
print(conhull)
if len(conhull) < 4:
    print(0)
else:
    total = 0
    for cx, cy in soviets:
        # print(cx, cy)
        within = True
        for i in range(len(conhull)):
            ax, ay = conhull[i-1]
            bx, by = conhull[i]

            sign = ((ax-cx) * (by-cy)) - ((ay-cy) * (bx-cx))
            # print(sign)
            if sign < 0:
                within = False
        
        if within:
            total += 1

    print(total)


