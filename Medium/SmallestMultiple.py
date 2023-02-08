def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a,b)                ## IMPORTANT - NEEDS TO BE FLOOR DIV


def smallest(nums):
    multiple = nums[0]
    for i in nums[1:]:
        multiple = lcm(multiple, i)

    return multiple


if __name__ == '__main__':
    while True:
        try:
            nums = list(map(int, input().split()))
            print(int(smallest(nums)))
        except:
            break
