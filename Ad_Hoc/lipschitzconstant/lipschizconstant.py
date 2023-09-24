N = int(input())

points = []
for _ in range(N):
    x, z = map(float, input().split())
    points.append((x,z))
points.sort()


big = -1
for i in range(1, N):
    zdiff = abs(points[i][1] - points[i-1][1])
    xdiff = abs(points[i][0] - points[i-1][0])
    
    big = max(big, zdiff/xdiff)

print(big)
    