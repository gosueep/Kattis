t = int(input())

for _ in range(t):
    line = input().strip()
    
    l = 1
    while l < len(line):
        start = line[:l]
        next = int(start)+1
        np = next + 1
        
        next = str(next)
        np = str(np)
        
        print(line[l:len(next)+1], next)
        if line[l:len(next)] == next:
            break
        
        print(line[l:len(np)])
        break
    
    print(start, next, np)
    
    