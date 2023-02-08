def inflation(cans):
    b = 1
    minFrac = 1
    for i in sorted(cans):
        if i > b:
            return 'impossible'
        elif i < b:
            currFrac = i / b
            if currFrac < minFrac:
                minFrac = currFrac
        b += 1

    return minFrac


if __name__ == '__main__':
    n = int(input())
    cans = list(map(int, input().split()))

    print(inflation(cans))
