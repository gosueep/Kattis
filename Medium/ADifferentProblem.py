# https://open.kattis.com/problems/different

import sys

for line in sys.stdin:

    num1, num2 = line.split()

    print(abs(int(num1) - int(num2)))