from itertools import permutations
n=input();f=lambda x:int(''.join(x))
p=[f(x)for x in permutations(n)if f(x)>int(n)]
print([0,min(p)][len(p)>0])