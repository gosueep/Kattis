N = int(input())

for _ in range(N):
    line = input()
    msg = [ord(x) - ord('a') + 1 if x != ' ' else 0 for x in line[2:]]
    
    output = ''
    if line[0] == 'e':
        prev = 0
        for num in msg:
            num += prev
            prev = num
            num = num % 27
            
            if num == 0:
                output += ' '
            else:
                output += chr(num - 1 + ord('a'))
    else:
        prev = 0
        for num in msg:
            if num == prev:
                c = ' '
            elif num > prev:
                res = num - prev
                c = chr(res - 1 + ord('a'))
            else:
                res = 27 - (prev - num)
                c = chr(res - 1 + ord('a'))
            prev = num
            output += c
        
    print(output)