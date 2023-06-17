from collections import defaultdict

n = int(input())
nums = map(int, input().split())

d = defaultdict(int)

total = 0
for i in nums:
    d[i] += 1
    if i+1 == d[i]:
        d[i] = 0
        total += i+1
# print(total)
for i in d:
    if d[i] != 0:
        total += i+1
print(total)
