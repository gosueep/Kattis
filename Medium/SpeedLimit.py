# https://open.kattis.com/problems/speedlimit

inputs = int(input())

while inputs != -1:

    speeds = []
    miles = []

    for _ in range(inputs):
        speed, mark = map(int, input().split())
        speeds.append(speed)
        miles.append(mark)

    length = 0
    for i in range(len(speeds)):
        if i == 0:
            length += speeds[i] * miles[i]
        else:
            length += speeds[i] * (miles[i] - miles[i-1])

    print(f'{length} miles')

    inputs = int(input())
