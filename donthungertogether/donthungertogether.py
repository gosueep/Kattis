import math 

n,k = map(int, input().split())

dp = [[0,0] for _ in range(n)]
dp_bool = [False for _ in range(n)]
for i in range(n):
    q,exp = map(int, input().split())

    for j in range(exp):
        if i+j < n:
            dp[i+j][0]+= q
            dp[i+j][1]+= 1
        else:
            break
    if i+j < n:
        dp_bool[i+j] = True
    # print(i+j)

# print(dp)
# print(dp_bool)
dp_bool[-1] = True

possible = True
minfood = math.inf
nights = 1
for i in range(n):
    if dp[i][0] == 0:
        possible = False
        break
    if dp_bool[i] == True:
        if minfood > dp[i][0]:
            minfood, nights = dp[i]
        elif minfood == dp[i][0]:
            nights = min(nights, dp[i][1])

if possible:
    print(minfood / nights / k)
else:
    print(-1)
        
    