n = int(input())

a, b, c  = 1, 1, 2

for i in range(n):
    a, b, c = b, c, a+b+c
    
# print(a, b, c)
print(a % int(1e6))