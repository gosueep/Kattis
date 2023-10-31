import math
a,n = map(float, input().split())

# (a/math.pi) ** 0.5
# 2 pi r

if ((a/math.pi) ** 0.5) * 2 * math.pi <= n:
    print('Diablo is happy!')
else:
    print('Need more materials!')