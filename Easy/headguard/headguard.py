while True:
    try:
        line = input()
    except:
        break

    out = []
    i = 0
    while i < len(line):
        j = i
        while j < len(line) and line[i] == line[j]:
            j += 1
        out.append(str(j-i) + line[i])
        i = j
    print(''.join(out))
