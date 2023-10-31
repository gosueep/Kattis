import math

for _ in range(int(input())):
    origin = tuple(map(float, input().split()))
    N = int(input())
    
    dark = True
    for i in range(N):
        p = tuple(map(float, input().split()))
        if math.dist(origin, p) <= 8:
            dark = False
    if dark:
        print('curse the darkness')
    else:
        print('light a candle')