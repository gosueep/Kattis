N = int(input())
nums = list(map(int, input().split()))
low, high = map(int, input().split())

nums.sort()

a,b = -1,-1
maxdiff = -1
for i in range(1,N):
    x,y = nums[i-1], nums[i]
    girl = (x+y)//2
    print(girl)
    
    if girl % 2 == 0:
        girl -= 1
        
    
    if low <= girl and girl <= high:        
        diff = min(y-girl, girl-x)
        print(diff)
        
        if diff > maxdiff:
            a,b = x,y
            maxdiff = diff

print(a,b)
print(maxdiff)