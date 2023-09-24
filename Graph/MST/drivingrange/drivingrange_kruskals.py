
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())

    q = []
    for _ in range(M):
        src, dest, w = map(int, input().split())
        q.append((src, dest, w))
    q.sort(key=lambda x: x[2])

    mst = set()  # stores seen nodes
    for a,b,w in q:
        if a not in mst or b not in mst:
            mst.add(a)
            mst.add(b)
        if len(mst) == N:
            break

    if len(mst) != N:
        print('IMPOSSIBLE')
    else:
        print(w)