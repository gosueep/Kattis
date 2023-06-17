length, numcolors = map(int, input().split())
colors = map(int, input().split())

d = {}
for i in range(1, numcolors+1):
    d[i] = 0


for c in colors:
    d[c] += 1

least = min([d[i] for i in d])
choices = []
for i in d:
    if d[i] == least:
        choices.append(i)

print(len(choices))
for i in sorted(choices):
    print(i, end=' ')