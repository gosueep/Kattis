import sys;input=sys.stdin.readline;N,M=map(int,input().split());s,w=set(),0
for a,b,w in sorted([list(map(int,input().split()))for _ in'.'*M],key=lambda x:x[2]):
 if not(a in s and b in s):s.update([a,b])
 if len(s)==N:break
print([w,'IMPOSSIBLE'][len(s)!=N])