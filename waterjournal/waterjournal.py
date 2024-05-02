n,a,b = map(int, input().split())

log = set([int(input()) for x in range(n-1)])

if a not in log and b not in log:
    print(-1)
elif a not in log:
    print(a)
elif b not in log:
    print(b)
else:
    print('\n'.join([str(x) for x in range(a,b+1)]))
    
    