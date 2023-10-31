import math


radii = [20,40,60,80,100,120,140,160,180,200]
origin = (0,0)

for _ in range(int(input())):
    score = 0
    for i in range(int(input())):
        p = tuple(map(float, input().split()))
        
        d = abs(math.dist(origin, p))
        
        i = 0
        while i < len(radii) and d > radii[i]:
            i += 1
        if i < len(radii):
            score += (10-i)
    
    print(score)