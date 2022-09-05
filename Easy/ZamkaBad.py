# Zamka
# https://open.kattis.com/problems/zamka


def digitSum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10

    return sum


def zamka(lower, upper, sum):

    sumRem = sum - digitSum(int(lower))

    lower = list(lower)
    print(lower)

    i = 0
    while sumRem > 0:
        currDigit = int(lower[i])
        lower[i] = sumRem % 9
        sumRem -= 9 - currDigit

    return lower


if __name__ == "__main__":
    L = input()     # lower bound
    D = input()     # upper bound
    X = int(input())     # sum

    print(zamka(L, D, X))
