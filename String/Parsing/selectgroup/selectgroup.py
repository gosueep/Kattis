groups = {}
stack = []

def parse():
    
    token = stack.pop()
    
    if token == 'union':
        s1 = parse()
        s2 = parse()
        return s1 | s2
    elif token == 'intersection':
        s1 = parse()
        s2 = parse()
        return s1 & s2
    elif token == 'difference':
        s1 = parse()
        s2 = parse()
        return s1 - s2
    else:
        return groups[token]


while True:
    try:
        line = input().split()
        
        if line[0] == 'group':
            name = line[1]
            ppl = line[3:]
            groups[name] = set(ppl) 
        else:
            stack = list(reversed(line))
            result = parse()
            print(' '.join(sorted(result)))
        
    except:
        break