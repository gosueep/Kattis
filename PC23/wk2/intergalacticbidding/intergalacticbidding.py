N, target = map(int, input().split())
names = {}
bids = [0]
for _ in range(N):
    name, bid = input().split()
    bid = int(bid)
    names[bid] = name
    bids.append(bid)

bids.sort(reverse=True)

winners = []
for i in bids:
    if i <= target:
        target -= i
        winners.append(i)
    
    if target == 0:
        break

if target == 0:
    print(len(winners))
    for i in winners:
        print(names[i])
else:
    print(0)    
    
    