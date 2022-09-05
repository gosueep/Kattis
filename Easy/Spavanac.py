# Spavanac
# https://open.kattis.com/problems/spavanac

hours, minutes = map(int, input().split())

if minutes < 45:
    print((hours - 1) % 24, end=' ')
else:
    print(hours, end=' ')

print((minutes - 45) % 60)
