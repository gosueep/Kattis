import math
for _ in'_'*int(input()):
 o=tuple(map(float,input().split()));d=1
 for i in'_'*int(input()):
  if math.dist(o,tuple(map(float, input().split())))<=8:d=0
 print(['light a candle','curse the darkness'][d])