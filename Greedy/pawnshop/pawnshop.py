from collections import defaultdict

N = int(input())
orig = list(map(int, input().split()))
rearr = list(map(int, input().split()))


oset = defaultdict(int)
rset = defaultdict(int)
parts = set()
for i in range(N):
    oset[orig[i]] += 1
    rset[rearr[i]] += 1
    
    if oset == rset and i != N-1:
        oset.clear()
        rset.clear()
        parts.add(i)

for i in range(N):
    print(rearr[i], end=" ")
    if i in parts:
        print("#", end=" ")
        