from geometry import *

def printP(p):
    print("{:.2f}".format(p.x + 0.0) + " " + "{:.2f}".format(p.y + 0.0), end=" ")

for _ in range(int(input())):
    x1, y1, x2, y2, x3, y3, x4, y4 = [float(x) for x in input().split()]
    p1, p2, p3, p4 = Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)
    l1, l2,  v1, v2 = Line.fromPoints(p1, p2), Line.fromPoints(p3, p4), Vector.fromPoints(p1, p2), Vector.fromPoints(p3,p4)
    
    
    if l1.isSameAs(l2):
        
        print(p1, p2, p3, p4)
        
        ps = []
        for p in [p1, p2]:
            if p.x >= p3.x and p.x <= p4.x:
                ps.append(p)
        
        for p in [p3, p4]:
            if p.x >= p1.x and p.x <= p2.x:
                ps.append(p)
        print(ps)
        printP(Point(x1, y1))
        printP(Point(x2, y2))
        print()
    elif l1.intersectAt(l2): 
        # print(l1.intersectAt(l2))
        printP(l1.intersectAt(l2))
        print()
    else:
        print("none")