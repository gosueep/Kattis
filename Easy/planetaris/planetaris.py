sys, ships = map(int, input().split())
finni = map(int, input().split())

wins = 0

for i in sorted(finni):
    if i+1 <= ships:
        wins += 1
        ships -= i+1

print(wins)