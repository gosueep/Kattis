_,M=map(int,input().split())
d=[0]*M
for c in input().split():d[int(c)-1]+=1
x=[str(i+1)for i in range(M)if d[i]==min(d)]
print(len(x))
print(' '.join(x))