from collections import deque

for _ in range(int(input())):
    out = deque()
    temp = deque()
    front = False
    
    def pushtemp():
        while temp:
                out.appendleft(temp.pop())
    
    for i in input().strip():
        if i == ']':
            front = False
            pushtemp()
            
        elif i == '[':
            front = True
            pushtemp()
                
        elif i == '<':
            if front:
                if len(temp)>0:
                    temp.pop()
            else:
                if len(out)>0:
                    out.pop()
        else:
            if front:
                temp.append(i)
            else:
                out.append(i)
    pushtemp()
    print(''.join(out))