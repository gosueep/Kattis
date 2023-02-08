if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        numCities, numPilots = map(int, input().split())

        setBruh = set()

        for p in range(numPilots):
            a, b = map(int, input().split())
            setBruh.add(a)
            setBruh.add(b)

        print(len(setBruh)-1)
