for _ in range(int(input())):
    N = int(input())
    
    trie={}

    nums=[]
    for _ in range(N):
        nums.append(input())
    nums.sort(reverse=True)
        
    possible = True
    for num in nums:
        curr = trie
        for d in num[:-1]:
            if d in curr:
                curr = curr[d]
            else:
                curr[d] = {}
                curr = curr[d]
        
        d = num[-1]
        if d in curr:
            possible = False
            break
        else:
            curr[d] = {}
    
    if possible:
        print("YES")
    else:
        print("NO")