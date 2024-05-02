import re
n,m,q=map(int, input().split())
p=[input()for _ in range(n)]
r=['.']*m
for _ in range(q):
    i,b=input().split()
    r[int(i)-1]=b
x=re.findall(''.join(r),'\n'.join(p))
c=len(x)
print([f'unique\n{p.index(x[0])+1}',f'ambiguous\n{c}'][c>1])