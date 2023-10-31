from itertools import permutations

num = input()

ps = [int(''.join(x)) for x in permutations(num)]
num = int(num)

out = 0
for i in sorted(ps):
    if i > num:
        out = i
        break
print(out)
