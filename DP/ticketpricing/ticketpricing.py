N, W = map(int, input().split())

weeks = []
for _ in range(W+1):
    wk = list(map(int, input().split()))
    
    week=[]
    tickets = wk[0]
    for i in range(tickets):
        week.append((wk[1+i], wk[tickets+1+i]))
    weeks.append(week)

best = [0 for _ in range(W+1)]
dp = {}
def maxrev(wk, seats):
    
    # print(wk, rev, seats)
    if (wk,seats) in dp:
        return dp[(wk, seats)]
    
    if wk > W or seats == N:
        return 0
    
    r,bp = max([(p*min(s, N-seats) + maxrev(wk+1, min(seats + s, N)), p) for p,s in weeks[wk]], key=lambda x: x[0])
    best[wk] = bp
    
    dp[(wk,seats)] = r
    return r


# print('\n'.join(str(x) for x in weeks))
print(maxrev(0, 0))
# print(best)
print(best[0])