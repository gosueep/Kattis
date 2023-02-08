# https://open.kattis.com/problems/sevenwonders

from collections import defaultdict


def sevenwonders(cards):

    deck = defaultdict(int)

    for c in cards:
        deck[c] += 1

    score = 0
    for d in deck.values():
        score += d ** 2

    if len(deck) == 3:
        score += min(deck.values()) * 7

    return score


if __name__ == "__main__":
    print(sevenwonders(input()))