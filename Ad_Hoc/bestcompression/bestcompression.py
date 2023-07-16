import sys
input = sys.stdin.readline

N, b = map(int, input().split())

# print(N, 2**(b+1)-1)

if N <= 2**(b+1)-1:
    print('yes')
else:
    print('no')

## IMPORTANT - you can have files of less than size b
    # 000
    # 001
    # 010
    # 011
    # 100
    # 101
    # 110
    # 111
    
    # 00
    # 01
    # 10
    # 11
    
    # 0
    # 1
    
    # _