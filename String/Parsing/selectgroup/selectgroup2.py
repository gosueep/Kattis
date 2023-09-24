import sys
groups = {}

for line in sys.stdin:
    line = line.split()
    
    if line[0] == 'group':
        name = line[1]
        ppl = line[3:]
        groups[name] = set(ppl) 
    else:
        stack = list(reversed(line))
        
        for token in stack:
            if token == 'union':
                stack.append(groups[stack.pop()] | groups[stack.pop()])
            elif token == 'intersection':
                stack.append(groups[stack.pop()] & groups[stack.pop()])
            elif token == 'difference':
                s1, s2 = groups[stack.pop()], groups[stack.pop()]
                stack.append(s1 - s2)
        
        result = stack[0]
        print(' '.join(sorted(result)))