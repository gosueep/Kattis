# The Amazing Human Cannonball
# https://open.kattis.com/problems/humancannonball2

import math
g = 9.81


def humanball(v0, theta, x1, h1, h2):

    theta = theta / 180 * math.pi               # convert theta to radians
    t_wall = x1 / (v0 * math.cos(theta))        # time at wall
    y_wall = v0 * t_wall * math.sin(theta) - 0.5 * g * t_wall ** 2      # y_pos at wall

    if h1 + 1 < y_wall < h2 - 1:
        return "Safe"
    else:
        return "Not Safe"


if __name__ == "__main__":
    for i in range(int(input())):
        v0, theta, x1, h1, h2 = map(float, input().split())
        print(humanball(v0, theta, x1, h1, h2))
