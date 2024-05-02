line = input().strip()

l, r = line.split('()')
if l == r:
    print('correct')
else:
    print('fix')