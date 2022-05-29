# Trik
# https://open.kattis.com/problems/trik


# ball starts in leftmost cup
def borko(moves):

    cups = [1, 0, 0]

    for move in moves:
        if move == 'A':
            cups[0], cups[1] = cups[1], cups[0]     # swap 1st and 2nd cup
        elif move == 'B':
            cups[1], cups[2] = cups[2], cups[1]     # swap 2nd and 3rd cup
        elif move == 'C':
            cups[0], cups[2] = cups[2], cups[0]     # swap 1st and 3rd cup

    return cups.index(1) + 1


if __name__ == "__main__":
    print(borko(input()))
