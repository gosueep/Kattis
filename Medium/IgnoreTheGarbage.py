# https://open.kattis.com/problems/ignore

import sys

flipped = '0125986'

for line in sys.stdin:

    num = int(line)
    result = ''

    while num > 0:

        result += flipped[num % 7]
        num = num // 7

    print(result)


# num % 7 = leftmost digit
# num // 7 = 2nd digit
# ...


# 0 - 0
# 1) 1 - 1
# 2) 2 - 2
# 3) 5 - 5
# 4) 6 - 9
# 5) 8 - 8
# 6) 9 - 6
#
# 7) 10 - 01
# 8) 11 - 11
# 9) 12 - 51
# 10) 15 - 21
# 11) 16
# 12) 18
# 13) 19
#
# 14) 20 - 02
#
#
# 97) 199 - 661
# 98)  200 - 002
