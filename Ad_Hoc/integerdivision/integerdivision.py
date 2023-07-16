from collections import defaultdict

N, d = map(int, input().split())
nums = list(map(int, input().split()))

count = defaultdict(int)
for i in nums:
    count[i//d] += 1
    
pairs = 0
for i in count:
    c = count[i]
    if c > 1:
        pairs += c * (c-1) // 2   

print(pairs) 