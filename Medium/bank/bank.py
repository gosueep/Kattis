n, close = map(int, input().split())
ppl = [list(map(int, input().split())) for x in range(n)]


s = sorted(ppl, reverse=True)
times = set()
total = 0

for amt, t in s:

    while t in times:
        t -= 1

    if t < 0:
        continue

    total += amt
    times.add(t)

print(total)
