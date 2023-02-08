# https://open.kattis.com/problems/alphabetanimals

from collections import defaultdict

def animals(last, words):

    # start letter : word
    adjList = defaultdict(list)
    for w in words:
        adjList[w[0]].append(w)

    startLetter = last[-1]

    if startLetter in adjList:
        for word in adjList[startLetter]:

            lastLet = word[-1]

            if lastLet not in adjList:
                return word + "!"
            elif startLetter == lastLet and len(adjList[startLetter]) == 1:
                return word + "!"
        return adjList[startLetter][0]

    return "?"



if __name__ == "__main__":

    last = input()
    words = []
    for _ in range(int(input())):
        words.append(input())

    print(animals(last, words))
