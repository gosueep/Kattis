if __name__ == '__main__':
    while True:
        try:
            num = int(input())
            if num == 1:
                print(num)
            else:
                print(int(num) * 2 - 2)
        except Exception:
            break



