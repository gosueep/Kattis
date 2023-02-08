
if __name__ == '__main__':
    cases = int(input())
    for _ in range(cases):
        _ = input()

        csNum, econNum = map(int, input().split())
        compscis = list(map(int, input().split()))
        econs = list(map(int, input().split()))

        csAvg = sum(compscis) / csNum
        econAvg = sum(econs) / econNum

        total = 0
        for c in compscis:
            if csAvg > c > econAvg:
                total += 1

        print(total)








