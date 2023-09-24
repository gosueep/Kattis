
if __name__ == '__main__':
    numInvs, amtNeeded = map(int, input().split())
    invs = []
    for _ in range(numInvs):
        invs.append(list(map(int, input().split())))

    minDays = 10**10
    start, stop = 0, 10**9+1
    while start <= stop:
        mid = (stop + start) // 2

        total = 0
        for dayReturn, initCost in invs:
            roi = dayReturn * mid - initCost
            if roi > 0:
                total += roi

        if total < amtNeeded:
            start = mid + 1
        elif total > amtNeeded:
            stop = mid - 1
            if mid < minDays:
                minDays = mid
        else:
            minDays = mid
            break

    print(minDays)
