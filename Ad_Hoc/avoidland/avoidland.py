N = int(input())

hori = []
vert = []
moves = 0
for _ in range(N):
    i, j = map(int, input().split())
    hori.append(i)
    vert.append(j)
hori.sort()
vert.sort()

for i in range(N):
    moves += abs(hori[i] - (i+1))
    moves += abs(vert[i] - (i+1))

print(moves)