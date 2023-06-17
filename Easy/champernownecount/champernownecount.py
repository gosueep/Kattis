n, k = map(int, input().split())

divisible = 0
rem = 0
for i in range(1, n+1):
    rem = rem * (10 ** (len(str(i)))) + i
    rem = rem % k
    if rem == 0:
        divisible += 1
print(divisible)