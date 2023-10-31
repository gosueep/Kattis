N = int(input())
prices = list(map(int, input().split()))
prices.sort(reverse=True)
disc = 0
for i in range(N):
    if (i+1) % 3 == 0:
        disc += prices[i]
print(disc)