palis = []
digits = '0123456789'
for i in digits:
    for j in digits:
        for k in digits:
            palis.append(int(i+j+k + k+j+i))
for _ in range(int(input())):
    n = int(input())
    print(min(palis, key=lambda x: abs(n-x)))