import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    i, num = input().split()
    
    # Check if possible to be octal
    possible = True
    for d in num:
        if d == '9' or d == '8':
            possible = False
    
    # If possible, convert to octal, else 0
    octal = int(num, 8) if possible else 0
    
    # print the output
    print(f'{i} {octal} {int(num)} {int(num, 16)}')