n = int(input())
ax, ay = map(int, input().split())
bx, by = map(int, input().split())

moves = [list(map(int, input().split())) for _ in range(n)]

# print(n)
# print(moves)

def endgame(ax, ay, bx, by):

    aset = set()
    for dx, dy in moves:
        nx, ny = ax + dx, ay + dy
        if 0 < nx <= n and 0 < ny <= n:
            aset.add((nx, ny))

    # print(aset)

    bset = set()
    for dx, dy in moves:
        nx, ny = bx - dx, by - dy
        if 0 < nx <= n and 0 < ny <= n:
            bset.add((nx, ny))
            if (nx, ny) in aset:
                return 1

    # print(bset)
    return 0

# alice
awin = endgame(ax, ay, bx, by)

bwin = endgame(bx, by, ax, ay)

if awin:
    print('Alice wins')
elif bwin:
    print('Bob wins')
else:
    print(f'tie {ax} {ay}')  