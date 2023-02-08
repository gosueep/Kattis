N = int(input())

for i in range(N):

    num = int(input())
    result = 1
    for j in range(1, num+1):
        result = (result * j) % 10

    print(result)