N, Q = map(int, input().split())

cities = {}

i = 0
for x in list(map(int, input().split())):
    i += 1
    cities[i] = x


for i in range(Q):
    qtype, a, b = map(int, input().split())

    if qtype == 1:
        cities[a] = b
    elif qtype == 2:
        print(abs(cities[a] - cities[b]))
