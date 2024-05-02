from functools import lru_cache

N, bobname = input().split()
amt ={}
for _ in range(N):
    name, t = input().split()
    amt[name] = t

print(amt)

@lru_cache(maxsize=None)
def recursive(name):
    
    if no name or :
        return 0
    
    for p in names:
        if name.startswith(p):
            # return amt[p] * recursive(rest of name)
            return amt[p] * recursive(name[len(p)])
        
print(recursive(bobname))