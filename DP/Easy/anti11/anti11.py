dp = [[1, 1]]
ans = [0]
for i in range(10000):
    zeros, ones = dp[-1]
    dp.append([ones + zeros, zeros])
    ans.append((zeros + ones) % (int(1e9) + 7))

for _ in range(int(input())):
    i = int(input())
    print(ans[i])
    