N, D, R = map(int, input().split())
dam = list(map(int, input().split()))
res = set(map(int, input().split()))

unable = 0
for i in dam:
    if i-1 in res:
        res.remove(i-1)
    elif i+1 in res:
        res.remove(i+1)
    else:
        unable += 1
print(unable)