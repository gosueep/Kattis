n, k = map(int, input().split())
d, s = map(int, input().split())

result = (d*n - k*s) / (n-k)

if 0 <= result <= 100:
    print(result)
else:
    print('impossible')
