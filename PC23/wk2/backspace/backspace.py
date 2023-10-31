# https://open.kattis.com/problems/backspace

from collections import defaultdict


def backspace(stream):

    stack = []

    for s in stream:
        if s == '<' and len(stack) > 0:
            stack.pop()
        else:
            stack.append(s)

    return ''.join(stack)


if __name__ == "__main__":
    print(backspace(input()))