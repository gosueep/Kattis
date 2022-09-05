# https://open.kattis.com/problems/sibice

matches, width, height = map(int, input().split())

hypot = (width**2 + height**2) ** 0.5

for _ in range(matches):
    length = int(input())
    print("DA") if length <= hypot else print("NE")



