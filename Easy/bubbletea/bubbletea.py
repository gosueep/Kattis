N = int(input())
teaPs = list(map(int, input().split()))
M = int(input())
topPs = list(map(int, input().split()))

prices = []
for i in range(0, N):
    p = teaPs[i] + min(topPs[x-1] for x in list(map(int, input().split()))[1:])
    prices.append(p)

students = int(input()) // min(prices) - 1
if students < 0:
    print(0)
else:
    print(students)
