parts, days = map(int, input().split())

seen = set()
for i in range(days):
    seen.add(input())
    if len(seen) >= parts:
        print(i+1)
        exit()
print('paradox avoided')