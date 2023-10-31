import math

n,r,w,h = map(int, input().split())
r2 = r**2

points = [tuple(map(int, input().split())) for _ in range(n)]
rect = [(0,0), (0,h), (w,0), (h,w)]

def intersect(center, radius, pts):
    r2 = r*r/2
    d = 


areas={}
for p in points:
    x,y,z = p
    circle = math.pi * r2
    if x+r <=w and x-r >= 0 and y+r <= h and y-r <= w:
        areas[p] = circle
    else:
        if x+r > w:
            
        

print(ev)