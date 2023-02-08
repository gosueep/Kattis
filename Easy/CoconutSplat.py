

def coconut(s, n):
    game = []

    for p in range(n):
        game.append([3, p+1])

    currPlayer = 0

    while len(game) > 1:

        currPlayer = (currPlayer + s-1) % (len(game))
        game[currPlayer][0] -= 1

        if game[currPlayer][0] == 2:
            game.insert(currPlayer, [2, game[currPlayer][1]])
        elif game[currPlayer][0] == 0:
            game.pop(currPlayer)
            currPlayer = currPlayer % len(game)
        else:
            currPlayer = (currPlayer + 1) % len(game)

    return game[0][1]


if __name__ == "__main__":
    s, n = map(int, input().split())
    print(coconut(s, n))
