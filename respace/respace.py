line = input()
N = len(line)
d=set(input().split())

def recurse(l,r):    
    
    if l==r:
        return 0
    if line[l:r] in d:
        return 0
    
    x = min(r-i + recurse(r,N) for i in range(l,r))
    
    print(x)

print(recurse(0,N))