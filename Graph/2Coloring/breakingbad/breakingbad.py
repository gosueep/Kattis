from collections import defaultdict, deque
# 2 coloring

N = int(input())
items = [input() for _ in range(N)]

M = int(input())
adj = defaultdict(list)
for _ in range(M):
    a,b =input().split()
    adj[a].append(b)
    adj[b].append(a)

coloring = [set(), set()]
seen = set()

possible = True
for i in items:
    if i in seen:
        continue
    q = deque([(i, 0)])
    while q:
        curr, color = q.popleft()
        if curr in coloring[1-color]:    # if already colored other color, false
            possible = False
            break
        seen.add(curr)
        coloring[color].add(curr)
        for a in adj[curr]:
            if a not in seen:
                q.append((a, 1-color))
                coloring[1-color].add(a)
        
if possible:
    for x in coloring:
        print(' '.join(i for i in x))
else:
    print('impossible')