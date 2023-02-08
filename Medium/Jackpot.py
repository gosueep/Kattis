
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def jackpot(wheels):

    multiple = wheels[0]

    for w in wheels[1:]:
        multiple = int(lcm(multiple, w))

    return multiple


if __name__ == '__main__':
    for _ in range(int(input())):
        numWheels = int(input())
        wheels = list(map(int, input().split()))

        spins = jackpot(wheels)

        if spins > 10 ** 9:
            print("More than a billion.")
        else:
            print(spins)
