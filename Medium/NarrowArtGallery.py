from collections import deque

# row : value
memo = {}
def narrow(gallery, row, k):

    if row < 0:
        return 0

    # left
    left = gallery[row][1] + narrow(gallery, row-1, k-1)

    # right
    right = gallery[row][0] + narrow(gallery, row-1, k-1)

    # none
    none = gallery[row][0] + gallery[row][1] + narrow(gallery, row-1, k)


    return max(left, right, none)


if __name__ == '__main__':
    rows, blocks = map(int, input().split())
    gallery = []
    for _ in range(rows):
        gallery.append(list(map(int, input().split())))

    x = narrow(gallery, rows-1, blocks)
    print(x)

