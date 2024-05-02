num = input()
s = set([int(i) for i in num])
comp = set({0,1,2,3,4,5,6,7,8,9})
for i in s:
    comp.remove(i)

if comp == {0}:
    print(0)
elif len(s) < 10:
    left = int(num[0])
    
    up = left
    l = len(num)-1
    while up in s:
        up += 1
        # print(up)
        if up >= 10:
            up = 0
            l += 1
    upnum = int(str(up) + str(min(comp))*l)
    
    down = left
    l = len(num)-1
    while down in s:
        down -= 1
        if down < 0:
            down = 9
            l -= 1
    dnum = int(str(down) + str(max(comp))*l)
        
    
    num = int(num)
    updiff = upnum - num
    downdiff = num - dnum
    
    print(up, down)
    print(dnum, downdiff)
    print(upnum, updiff)
    
    if updiff < downdiff or dnum < 0:
        print(upnum)
    elif updiff > downdiff:
        print(dnum)
    else:
        print(dnum, upnum)
else:
    print('Impossible')