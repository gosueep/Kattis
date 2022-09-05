# # Stopwatch
# # https://open.kattis.com/problems/stopwatch

def stopwatch(presses):

    time = 0
    prev = 0
    while presses > 0:
        curr = int(input())
        if presses % 2 == 1:
            time += curr - prev

        prev = curr
        presses -= 1

    return time


if __name__ == "__main__":
    presses = int(input())
    if presses % 2 == 1:
        print("still running")
    else:
        print(stopwatch(presses))
