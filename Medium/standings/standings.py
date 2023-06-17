for _ in range(int(input())):
    _ = input()
    n = int(input())

    seen = set()
    unfilled = []
    for i in range(n):
        _, rank = input().split()
        rank = int(rank)
        if rank in seen:
            unfilled.append(rank)
        else:
            seen.add(rank)
    
    unfilled.sort()
    u = 0
    badness = 0
    for i in range(1,n+1):
        if i not in seen:
            badness += abs(unfilled[u] - i)
            u += 1
    print(badness)