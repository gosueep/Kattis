N=int(input());r=list(map(int,input().split()));p={};l=N
for i in range(N):
 a=r[i]
 if a in p:l=min(l,i-p[a])
 p[a]=i
print(l)