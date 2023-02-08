# https://open.kattis.com/problems/guess


def Guess():

    start, stop = 1, 1000

    ans = ""
    while ans != 'correct':
        guess = int((stop + start) / 2)
        print(guess, flush=True)

        ans = input()

        if ans == 'lower':
            stop = guess-1
        elif ans == 'higher':
            start = guess+1


if __name__ == "__main__":
    Guess()
