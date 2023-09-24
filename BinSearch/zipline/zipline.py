import math

for _ in range(int(input())):
    w,g,h,rider = map(int, input().split())
    
    def cable(x):
        l1 = math.hypot(x, g-rider)
        l2 = math.hypot(w-x, h-rider)
        return l1+l2
    
    minlen = math.hypot(h-g, w)
    l,r = 0,w
    while r-l > 10**-6:
        x = (r-l)/3
        cl = cable(x+l)
        cr = cable(r-x)
        
        if cl < cr:
            r = r-x
        else:
            l = x+l

    print(minlen, cable(l))