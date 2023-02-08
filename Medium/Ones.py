# https://open.kattis.com/problems/ones

def ones(num):

    digits, multiple = 0, num

    while multiple != 0:

        if multiple % 10 == 1:
            multiple = multiple // 10
            digits += 1
        else:
            multiple += num

    return digits


if __name__ == "__main__":
    while True:
        try:
            print(ones(int(input())))
        except:
            break
