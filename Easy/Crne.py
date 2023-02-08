# https://open.kattis.com/problems/crne

# https://open.kattis.com/problems/crne

def crne_floor(n):
    if n % 2 == 0:
        pieces = (n//2 + 1) ** 2
    else:
        pieces = (n//2 + 1) ** 2 + (n//2 + 1)

    return int(pieces)


def crne(n):
    if n % 2 == 0:
        pieces = (int(n/2) + 1) ** 2
    else:
        pieces = ((n-1)/2 + 1) ** 2 + ((n-1)/2 + 1)
    return int(pieces)


if __name__ == "__main__":
    n = int(input())
    print(crne(n))
    print(crne_floor(n))
