
if __name__ == '__main__':
    cans, colors = map(int, input().split())
    sizes = []
    for _ in range(cans):
        sizes.append(int(input()))
    sizes.sort()

    # print(sizes)

    wasted = 0
    for _ in range(colors):
        needed = int(input())
        start, stop = 0, cans-1
        mid = 0
        while start <= stop:
            mid = (stop + start) // 2

            if sizes[mid] == needed:
                break
            elif sizes[mid] < needed:
                start = mid+1
            elif sizes[mid] > needed:
                stop = mid-1
        while sizes[mid] < needed:
            mid += 1
        wasted += sizes[mid] - needed

    print(wasted)


