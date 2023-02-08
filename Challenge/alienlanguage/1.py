def convertDec(num, system):
    decimal = 0
    base = len(system)
    exp = 0

    for n in reversed(num):
        decimal += (base ** exp) * system[n]
        exp += 1

    return decimal


def convertBase(dec, system):

    base = len(system)

    exp = 0
    while dec >= (base ** exp):
        exp += 1
    exp -= 1

    converted = []
    while exp >= 0:
        curr = (base ** exp)
        amt = dec // curr
        dec -= amt * (base ** exp)
        converted.append(system[amt])
        exp -= 1

    return ''.join(converted)


if __name__ == '__main__':
    cases = int(input())

    for case in range(cases):
        num, src, target = input().split()

        sMap = {}
        for i, s in enumerate(src):
            sMap[s] = i

        tMap = {}
        for i, x in enumerate(target):
            tMap[i] = x

        decNum = convertDec(num, sMap)
        converted = convertBase(decNum, tMap)
        print(f'Case #{case+1}: {converted}')






