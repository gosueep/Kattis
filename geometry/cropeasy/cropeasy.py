# find center of triangle by (x1 + x2 + x3)/3, same with y

import math

for case in range(int(input())):
    N,a,b,c,d,x,y,m = map(int, input().split())
    
    points = [(x,y)]
    for i in range(1,N):
        x = (a*x + b) % m
        y = (c*y + d) % m
        points.append((x,y))
    
    count = 0
    for i in range(N):
        xi, yi = points[i]
        for j in range(i+1, N):
            xj, yj = points[j]
            for k in range(j+1,N):
                xk, yk = points[k]
                if (xi + xj + xk) % 3 == 0 and (yi + yj + yk) % 3 == 0:
                    count += 1
    
    print(f'Case #{case+1}: {count}')