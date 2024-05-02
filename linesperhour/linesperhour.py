n, lph = map(int, input().split())
total = lph * 5

lines = [int(input()) for x in range(n)]
lines.sort()


p = 0
for i in lines:
    if total-i >= 0:        # OFF BY ONE - BE CAREFUL AHHHH
        total -=i
        p +=1
    else:
        break
print(p)