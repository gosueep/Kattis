N = int(input())

for _ in range(N):
    msg = input()
    shortest = N
    for k in range(1, N):
        prefix = msg[:k]
        i = k
        print(k, prefix)
        
        possible = True
        while i < N-k:
            curr = msg[i:i+k]  
            print(i, prefix, curr)
            if prefix != curr:
                possible = False
                break
            i += k
        if possible:
            print("asdfas")
            shortest = k
            break
    break
        
    print(shortest)
            