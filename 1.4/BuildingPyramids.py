# Building Pyramids
# https://open.kattis.com/problems/pyramids


def pyramid(blocks, height):
    levelBlocks = height ** 2

    if blocks < levelBlocks:
        return 0

    return 1 + pyramid(blocks - levelBlocks, height + 2)


if __name__ == "__main__":
    blocks = int(input())
    print(pyramid(blocks, 1))
