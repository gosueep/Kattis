# https://open.kattis.com/problems/pivot

# Very Interesting speedup by putting in function
# http://mycode.doesnot.run/2018/04/11/pivot/

def pivot():
    length = int(input())
    pivot = list(map(int, input().split()))

    high = pivot[0]
    low = pivot[-1]
    highList = [0] * length
    lowList = [0] * length


    for i in range(length):

        if pivot[i] > high:
            high = pivot[i]
        if pivot[length-i-1] < low:
            low = pivot[length-i-1]

        highList[i] = high
        lowList[length-i-1] = low

    numPivots = 0
    for i in range(length):
        if highList[i] == lowList[i]:
            numPivots += 1

    print(numPivots)


if __name__ == "__main__":
    pivot()
