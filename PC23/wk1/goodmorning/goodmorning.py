import sys
input = sys.stdin.readline

possible = set()
adj = {
    1: [1,2,3,4,5,6,7,8,9,0],
    2: [2,3,5,6,8,9,0],
    3: [3,6,9],
    4: [4,5,6,7,8,9,0],
    5: [5,6,8,9,0],
    6: [6,9],
    7: [7,8,9,0],
    8: [8,9,0],
    9: [9,],
    0: [0]
}

for i in range(1,10):
    possible.add(i)
    two = i*10
    for j in adj[i]:
        possible.add(two+j)
        three = (two+j) * 10
        for k in adj[j]:
            possible.add(three + k)

N = int(input())
for _ in range(N):
    i = int(input())
    add = 0
    found = False
    while not found:
        for num in [i+add,i-add]:
            if num in possible: 
                print(num)
                found = True
                break
        add += 1