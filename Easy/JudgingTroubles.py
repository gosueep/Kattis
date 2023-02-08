# https://open.kattis.com/problems/judging

from collections import defaultdict

if __name__ == '__main__':
    n = int(input())
    dom = defaultdict(int)
    kattis = defaultdict(int)
    for _ in range(n):
        dom[input()] += 1
    for _ in range(n):
        kattis[input()] += 1

    overlap = 0
    for res in kattis:
        overlap += min(kattis[res], dom[res])

    print(overlap)
