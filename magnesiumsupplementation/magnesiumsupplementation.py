# factor fast???
n,maxdosage,pills = map(int, input().split())

p = n
out = set()
orig = p
factors = []
k = 2
while k**2 <= p:
    if p%k == 0:
        factors.append(k)
        factors.append(p//k)
    k+=1
factors.append(1)
factors.append(orig)

# print(factors)

for i in factors:
    if i <= maxdosage and n // i <= pills:
        out.add(i)


print(len(out))
print('\n'.join([str(x) for x in list(sorted(list(out)))]))
            
    