# https://open.kattis.com/problems/estimatingtheareaofacircle

import math
import sys

for line in sys.stdin:

    if line == '0 0 0\n':
        sys.exit()

    radius, total_marks, circle_marks = map(float, line.split())

    true_area = math.pi * (radius ** 2)
    estimate = (circle_marks / total_marks) * (radius * 2) ** 2

    print(true_area, estimate)
