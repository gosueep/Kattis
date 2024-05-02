N, E = map(int, input().split())
arr = list(map(int, input().split()))

s = set(arr)

corr = []
for i in range(1,N+1):
    if i not in s:
        corr.append(i)

def compress(arr):
    i = 1
    out = []
    l,r = arr[0],arr[0]
    while i < len(arr):
        if arr[i-1]+1 == arr[i]:
            r = arr[i]
        else:
            if l == r:
                out.append(str(l))
            else:
                out.append(f'{l}-{r}')
            
            l = r = arr[i]
        
        i += 1
    
    if l == r:
        out.append(l)
    else:
        out.append(f'{l}-{r}')

    return out

arr = compress(arr)
corr = compress(corr)
if len(arr) == 1:
    print(f'Errors: {arr[0]}')
else:
    print(f'Errors: {", ".join(arr[:-1])} and {arr[-1]}')
if len(corr) == 1:
    print(f'Correct: {arr[0]}')
else:
    print(f'Correct: {", ".join(corr[:-1])} and {corr[-1]}')
        