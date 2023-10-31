N,W=map(int,input().split());d={};a=[[*map(int,input().split())]for _ in'.'*(W+1)]
def m(w,s):
 if(w,s)in d:return d[w,s]
 if w>W or s==N:return 0
 x=a[w];l=x[0];d[w,s],d[0]=max([(x[i]*min(x[i+l],N-s)+m(w+1,min(s+x[i+l],N)),-x[i])for i in range(1,l+1)]);return d[w,s]
print(m(0,0));print(-d[0])


n,w,*l=eval(I:='map(int,input().split())')
exec(f'k,*a={I};l+=[[*zip(a,a[k:])]];'*-~w)
def R(i,s,d={}):
    if~((i,s)in d):d[i,s]=[0]if(i>w)else max(((v:=min(s,S))*P+R(i+1,s-v)[0],-P)for P,S in l[i])
    return d[i,s]
a,b=R(0,n)
print(a,-b)