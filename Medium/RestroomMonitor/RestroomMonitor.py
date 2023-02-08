from collections import defaultdict

stalls, people = map(int, input().split())
deadlines = defaultdict(lambda: [0, 0])
latest = -1

for i in range(people):
    d, needTP = input().split()
    d = int(d)

    latest = max(latest, d)

    if needTP == 'y':
        deadlines[d][0] += 1
    else:
        deadlines[d][1] += 1

ycurr, ncurr = deadlines[latest]
yes, no = [0, 0]
for i in range(latest, 1, -1):

    if i in deadlines:
        if yes > 1:
            ycurr = (yes-1) + latest[i-1][0]
            yes = 1

        if yes + no > stalls:
            ncurr = yes + no - stalls
    else:
        if yes > 1:
            yes -= 1
            if no + 1 > stalls:


    yes, no = ycurr, ncurr

if deadlines[1][0] <= 1 and sum(deadlines[1]) <= stalls:
    print('Yes')
else:
    print('No')
