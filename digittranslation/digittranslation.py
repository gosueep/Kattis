import math
from functools import lru_cache
import sys

sys.setrecursionlimit(2**30)

words = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
combos = {'zerone', 'oneight', 'twone', 'threeight', 'fiveight', 'sevenine', 'eightwo', 'eighthree', 'nineight'}

inp = input().strip()
N=len(inp)
r=N-1
l=r-1

dp = [[0,0] for _ in range(N)]
dp[-1] = [1,1]
options = 1
while l >= 0:
    line = inp[l:r]
    if line in combos:
        options *=2
    if line in words:
        dp[l][0] = 
    
    else:
        dp[l][0] = dp[l-1][0]+1
        dp[l][1] = dp[l-1][1]+1
        


# options = 1
# @lru_cache(maxsize=None)
# def recursive(start):
#     global options
    
#     line = inp[start:]
#     if line == '' or len(line) == 0:
#         return 0
#     if line in words:
#         return 1
    
#     swap = math.inf
#     for c in combos:
#         if line.startswith(c):
#             options *= 2
#     for w in words:
#         if line.startswith(w):
#             swap = 1 + recursive(start+len(w))
#     cut = 1 + recursive(start+1)
#     return min(swap, cut)

print(recursive(0))
print(options % 9302023)