

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

    print(startX, startY)

    angles = []

    for x, y in points:
        angle = 


