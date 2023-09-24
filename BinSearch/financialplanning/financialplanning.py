N, minAmt = map(int, input().split())

invs = []
for _ in range(N):
    daily,cost = map(int, input().split())
    invs.append((daily,cost))

mindays = 0
maxdays = 10**10

best = -1

while mindays <= maxdays:
    days = (mindays + maxdays) // 2
    total = 0
    for daily, cost in invs:
        money = daily*days - cost
        if money > 0:
            total += money
    
    if total < minAmt:
        mindays = days+1
    elif total >= minAmt:
        maxdays = days-1
        best = days

print(best)
            