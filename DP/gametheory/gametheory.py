
for _ in range(int(input())):
    N = int(input())
    jumps = list(map(int, input().split()))
    points = list(map(int, input().split()))
    
    dp = [[ 0 for _ in range(N)] for x in range(2)]
    
    for start in range(N-1, -1, -1):
        you = []
        opp = []
        i = start
        while i < N:
            u = points[start]
            o = points[start]
            nextSpace = i + jumps[start]
            if nextSpace < N:
                u += dp[1][nextSpace]
                o += dp[0][nextSpace]
            you.append(u)
            opp.append(o)
            i = nextSpace
            
        dp[0][start] = max(you)
        dp[1][start] = min(opp)
    
    # print(points)
    # print(jumps)
    # print(dp[0])
    # print(dp[1])
    # print()
    [print(x, end=" ") for x in dp[0]]
    print()