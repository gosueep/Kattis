n, k = map(int, input().split())
# print(len([i for ]))
divisible = 0
rem = 0
for i in range(1, n+1):
    rem = rem*10 ** (len(str(i))) + i
    rem = (rem+i) % k
    if not rem == 0:
        divisible += 1

x = [0 for i in range(n) if rem := ((rem*10 ** (len(str(i)))) + i+1)]

print(divisible)