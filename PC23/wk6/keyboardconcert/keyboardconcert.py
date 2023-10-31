import sys
input = sys.stdin.readline

N, M = map(int, input().split())
boards = []
for i in range(N):
    boards.append(set(map(int, input().split()[1:])))
notes = list(map(int, input().split()))

switch=-1
n=-1
while n<M-1:
    dist = []
    for b in range(N):
        broken = False
        for i in range(n+1, M):
            if notes[i] not in boards[b]:
                dist.append(i-1)
                broken = True
                break
        if not broken:
            dist.append(i)
            break
    best = max(dist)
    switch += 1
    n = best

print(switch)