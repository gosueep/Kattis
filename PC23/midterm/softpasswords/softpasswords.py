s,a = [input().strip() for _ in'**']

possible = [a]
for i in '0123456789':
    possible.append(a + i)
    possible.append(i + a)
x=''
for i in a:
    if i.isupper():
        x += i.lower()
    else:
        x += i.upper()
possible.append(x)

print(['No','Yes'][s in possible])
# print(possible)