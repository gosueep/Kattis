height, width, swat = map(int, input().split())

window = []
for x in range(height):
    window.append(list(input()))

# effective range = square of (swat - 2), not including borders of the window
erange = swat - 2

best = 0
bestPos = (0, 0)

for h in range(1, height - erange):
    for w in range(1, width - erange):

        kills = 0
        for kh in range(erange):
            for kw in range(erange):
                if window[h+kh][w+kw] == '*':
                    kills += 1

        if kills > best:
            best = kills
            bestPos = h-1, w-1

br, bc = bestPos

for r, c in [(0, 0), (0, erange+1), (erange+1, 0), (erange+1, erange+1)]:
    window[br+r][bc+c] = '+'

for s in range(1, erange+1):
    window[br][bc + s] = '-'
    window[br+swat-1][bc + s] = '-'

    window[br + s][bc] = '|'
    window[br + s][bc+swat-1] = '|'

print(best)
for x in window:
    print(''.join(x))