N=int(input())
arr=list(map(int,input().split()))
pos={}
level=N
for i in range(N):
    a = arr[i]
    if a in pos:
        level = min(level, i-pos[a])
    pos[a]=i
print(level)
        