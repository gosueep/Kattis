from itertools import chain, combinations

if __name__ == '__main__':

    expr = input()
    lefts = []
    pairs = []
    for index, i in enumerate(expr):
        if i == '(':
            lefts.append(index)
        elif i == ')':
            pairs.append((lefts.pop(), index))

    numPairs = len(pairs)

    powerset = chain.from_iterable(combinations(pairs, r) for r in range(numPairs + 1))
    outputs = set()
    for subset in powerset:
        parens = set()
        for j in subset:
            parens.add(j[0])
            parens.add(j[1])
        output = ""
        for index, c in enumerate(expr):
            if index not in parens:
                output += c
        outputs.add(output)

    outputs.remove(expr)
    for expr in sorted(list(outputs)):
        print(expr)
