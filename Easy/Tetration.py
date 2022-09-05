# Tetration
# https://open.kattis.com/problems/tetration

# Not needed for this, inverse tetration is N ^ (1/N)
def tetration(base, exp):
    if exp == 1:
        return base

    return base ** tetration(base, exp-1)


if __name__ == "__main__":
    N = float(input())
    print(N ** (1/N))
