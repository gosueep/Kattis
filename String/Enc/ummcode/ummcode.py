line = input().split()

msg = ''
for w in line:
    um = True
    word = ''
    for c in w:
        if not c.isalpha():
            continue
            
        if c == 'u':
            word += '1'
        elif c == 'm':
            word += '0'
        else:
            um = False
            break
        
    if um:
        msg += word

output = ''
for i in range(7, len(msg)+1, 7):
    output += chr(int(msg[i-7:i], 2))
    
print(output)
