n, p = map(int, input().split())
nums = list(map(int, input().split()))
best = [0 for x in range(n)]

for i, x in enumerate(nums):
    curr = x - p
    if i == 0:
        best[0] = max(curr, 0)
    else:
        best[i] = max(curr, curr + best[i-1])

print(max(best))
