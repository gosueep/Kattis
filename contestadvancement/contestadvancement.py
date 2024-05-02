from collections import defaultdict

n,k,c = map(int, input().split())

count = defaultdict(int)
adv = 0

rank = []
out = []
same = []
for r in range(n):
    t,s = map(int, input().split())
    # rank.append((t,s,r))
    
    
    if count[s] < c:
        out.append((t,s,r))
        adv += 1
    else:
        same.append((t,s,r))
    
    count[s] += 1
    
    if adv >= k:
        break
# print(out)
if adv < k:
    for i in range(k-adv):
        out.append(same[i])
# print(same)
# print(out)
out.sort(key= lambda x: x[2])
# print(out)
print('\n'.join([str(x[0]) for x in out]))