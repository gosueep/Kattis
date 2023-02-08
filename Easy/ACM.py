def ACM():
    problems = {}

    while True:
        line = input()
        if line == '-1':
            break

        time, p, status = line.split()
        if p not in problems:
            problems[p] = [0, False]
        if status == 'right':
            problems[p][0] += int(time)
            problems[p][1] = True
        else:
            problems[p][0] += 20

    score, correct = 0, 0
    for x in problems:
        if problems[x][1]:
            score += problems[x][0]
            correct += 1
    print(correct, score)


if __name__ == '__main__':
    ACM()
