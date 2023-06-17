n, m = map(int, input().split())
t = list(map(int, input().split()))
l = list(map(int, input().split()))

t.sort()
l.sort()

ti = len(t)-1
li = len(l)-1

possible = 0
while ti >= 0 and li >= 0:
    if l[li] >= t[ti]:
        possible += 1
        li -= 1
        ti -= 1
    else:
        ti -= 1

print(possible)

