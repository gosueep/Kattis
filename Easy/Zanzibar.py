# Stand on Zanzibar
# https://open.kattis.com/problems/zanzibar

def zanzibar(poplist):

    imports = 0

    for i in range(len(poplist) - 1):
        i += 1
        if poplist[i] > poplist[i - 1]:
            growth = poplist[i] - poplist[i-1] * 2
            if growth > 0:
                imports += growth

    return imports


if __name__ == "__main__":
    for i in range(int(input())):
        print(zanzibar(list(map(int, input().split()))))
