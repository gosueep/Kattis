# https://open.kattis.com/problems/heimavinna

ranges = input().split(';')

problems = 0

for r in ranges:

    ran = list(map(int, r.split('-')))

    if len(ran) > 1:
        problems += ran[1] - ran[0] + 1
    else:
        problems += 1

print(problems)
