
def gandalf(spell, sentence):

    if len(set(spell)) != len(set(sentence)):
        return False

    words = {}
    for i, w in enumerate(sentence):
        words[w] = spell[i]

    return spell == ''.join(words[w] for w in sentence)


if __name__ == '__main__':
    spell = input()
    sentence = input().split()
    print(gandalf(spell, sentence))
