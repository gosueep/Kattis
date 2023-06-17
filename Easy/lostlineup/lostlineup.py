A = ['1' for _ in range(int(input()))]
for i, x in enumerate(list(map(int, input().split()))):
    A[x+1] = str(i+2)
print(' '.join(A))