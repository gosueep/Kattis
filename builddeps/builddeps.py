from collections import defaultdict, deque

N = int(input())
adjlist = defaultdict(set)
nodes = []
toposort = []
for i in range(N):
    line = input().split(':')
    build = line[0]
    nodes.append(build)
    print(line)
    if len(build) > 1:
        for dep in line[1].split():
            adjlist[build].add(dep)
print(adjlist)

start = input()
seen = set()
q = deque([start])
while q:
    i = q.pop()
    seen.add(i)
    for adj in adjlist[i]:
        q.append(adj)
start = input()