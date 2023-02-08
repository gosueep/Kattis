def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def prsteni(num, divisors):
    for d in divisors:
        commonDiv = gcd(num, d)
        print(f'{int(num/commonDiv)}/{int(d/commonDiv)}')


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    prsteni(nums[0], nums[1:])