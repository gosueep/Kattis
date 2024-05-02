line = input()

v, y= 0,0
for i in line.strip():
    if i in ['a', 'e', 'i', 'o', 'u', 'y']:
        y+=1
        if i != 'y':
            v += 1
print(v,y)
    