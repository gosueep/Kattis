
if __name__ == '__main__':

    for _ in range(int(input())):
        numDigits = int(input())

        print(8 * pow(9, numDigits-1, 1000000007) % 1000000007)

