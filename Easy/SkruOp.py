# https://open.kattis.com/problems/skruop


volume = 7
instructions = int(input())
for _ in range(instructions):

    instruction = input()

    if instruction == 'Skru op!' and volume < 10:
        volume += 1
    elif instruction == 'Skru ned!' and volume > 0:
        volume -= 1

print(volume)
