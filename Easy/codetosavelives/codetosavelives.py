for _ in range(int(input())):
    one = ''.join(input().split())
    two = ''.join(input().split())
    print(' '.join(list(str(int(one) + int(two)))))