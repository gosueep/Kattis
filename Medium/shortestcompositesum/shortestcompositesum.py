n = int(input())

# b is odd, a is even
def comp(a, b):
    while b % 3 != 0 and b % 5 != 0:
        a -= 2
        b += 2
    return a, b

half = n // 2
if n % 2 == 0:
    output = [half, half] if half % 2 != 0 else [half-1, half+1]
else:
    a, b = half, half+1
    output = comp(a,b) if half % 2 == 0 else comp(b,a)

print(len(output))
for i in output:
    print(i, end=' ')