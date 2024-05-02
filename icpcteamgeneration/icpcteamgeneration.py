N = int(input())

ppl = []
for i in range(N):
    a,b = map(int, input().split())
    ppl.append((a,b))

# print(ppl)

teams = []
for i in range(1,N+1):
    ai, bi = ppl[i-1]
    # print(ai, bi)
    for j in range(i+1,N+1):
        aj, bj = ppl[j-1]
        # print(ai, bi, i)
        # print(aj, bj, j)
        # print(ai <= j and j <= bi, aj <= i and i <= bj)
        if ai <= j and j <= bi and aj <= i and i <= bj:
            # print('in')
            for k in range(j+1,N+1):
                ak, bk = ppl[k-1]
                if ai <= k and k <= bi and aj <= k and k <= bj and ak <= i and i <= bk and ak <= j and j <= bk:
                    teams.append((i,j,k))

# print(teams)
# teams = [(1,2,3), (4,5,6), (4,8,9), (6,10,11)]
T = len(teams)
best = 0
for i in range(1,T+2):
    take = bin(i)[2:]
    take = '0'*(T-1-len(take)) + take
    num = 0
    # print(take)
    
    seen = set()
    for j in range(len(take)):
        if take[j] == '1':
            possible = True
            for p in teams[j]:
                if p in seen: possible = False
            if possible:
                for p in teams[j]: seen.add(p)
                num += 1
    best = max(best, num) 
    
print(best)
