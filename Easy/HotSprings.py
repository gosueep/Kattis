# https://open.kattis.com/contests/tvbgqq/problems/hotsprings

def springs(t):

    t.sort()

    result = []

    while len(t) > 0:
        result.insert(0, t.pop())
        if len(t) > 0:
            result.insert(0, t.pop(0))

    return result


if __name__ == "__main__":
    n = int(input())
    temps = list(map(int, input().split()))
    for i in springs(temps):
        print(i, end=' ')