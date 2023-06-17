l, r = map(int, input().split())

if 2*r >= (2 * l ** 2) ** 0.5:
    print('fits')
else:
    print('nope')