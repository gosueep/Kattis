# https://open.kattis.com/problems/monk

def climb(distance, points):
    climbTime = 0
    for dist, time in points:
        slope = dist / time
        if distance - dist > 10 ** -6:
            climbTime += time
            distance -= dist
        else:
            climbTime += distance / slope
            break

    return climbTime


def monk(asc, desc):
    height = sum([x[0] for x in asc])
    bottom, top = 0, height

    while (top - bottom) > 10 ** -6:
        mid = (bottom + top) / 2

        upTime = climb(mid, asc)
        downTime = climb(height - mid, desc)

        if upTime > downTime:
            top = mid
        elif downTime > upTime:
            bottom = mid
        else:
            break

    mid = float('%.5f' % mid)
    return max(climb(mid, asc), climb(height - mid, desc))


if __name__ == "__main__":
    numAsc, numDesc = map(int, input().split())

    asc = [list(map(int, input().split())) for x in range(numAsc)]
    desc = [list(map(int, input().split())) for x in range(numDesc)]

    print(monk(asc, desc))
