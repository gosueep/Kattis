# https://open.kattis.com/problems/rsamistake
# prime factorization
# Make sure not to find sqrt

from collections import defaultdict

facts = defaultdict(int)
def prime_factorization(p):
    factors = []
    k = 2
    while k**2 <= p:
        while p % k == 0:
            factors.append(k)
            p = p//k
        k += 1
    if p > 1:
        factors.append(p)
    return factors


a, b = map(int, input().split())
afacts = prime_factorization(a)
bfacts = prime_factorization(b)
# print(afacts, bfacts)

facts = defaultdict(int)
for i in afacts:
    facts[i] += 1
for i in bfacts:
    facts[i] += 1

nocredit = False
for i in facts:
    if facts[i] > 1:
        nocredit = True
        break

if nocredit:
    print('no credit')
elif len(afacts) == 1 and len(bfacts) == 1:
    print('full credit')
else:
    print('partial credit')    