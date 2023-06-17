import math

numer, denom = map(int, input().split('/'))

numer -= denom * 32
numer *= 5
denom *= 9

gcd = math.gcd(numer, denom)

print(f'{numer//gcd}/{denom//gcd}')
