N = int(input())

s = -1
for _ in range(N):
    i = int(input())
    
    if s == -1:
        s = i
    else:
        if i%s == 0:
            print(i)
            s = -1
        