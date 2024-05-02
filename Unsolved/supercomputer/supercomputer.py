# from collections import defaultdict
import sys
from math import log, ceil

sys.setrecursionlimit(2**30)

class RMQ:
    def __init__(self, n):
        self.inf = float("inf")
        self.low, self.high = 0, n - 1
        self.sz = pow(2, int(ceil(log(n, 2))))
        self.dat = [self.inf] * (2 * self.sz - 1)

    def build(self, arr):
        # print(arr, self.low, self.high)
        return self.build_help(arr, self.low, self.high, 0)

    def build_help(self, arr, low, high, pos):
        # print(low, high)
        if low == high:
            # print(self.dat, pos)
            # print(self.dat[pos])
            self.dat[pos] = arr[low]
            return
        mid = (low + high) // 2
        self.build_help(arr, low, mid, 2 * pos + 1)
        self.build_help(arr, mid + 1, high, 2 * pos + 2)
        self.dat[pos] = self.dat[2 * pos + 1] + self.dat[2 * pos + 2]

    def update(self, idx, val):
        self.update_help(idx, self.low, self.high, 0, val)

    def update_help(self, idx, low, high, pos, val):
        if idx < low or idx > high:
            return
        if low == high:
            self.dat[pos] = val
            return
        mid = (low + high) / 2
        self.update_help(idx, low, mid, 2 * pos + 1, val)
        self.update_help(idx, mid + 1, high, 2 * pos + 2, val)
        self.dat[pos] = self.dat[2 * pos + 1] + self.dat[2 * pos + 2]

    def query(self, qlow, qhigh):
        return self.query_help(qlow, qhigh, 0, self.high, 0)

    def query_help(self, qlow, qhigh, low, high, pos):
        if qlow <= low and qhigh >= high:  # TOTAL OVERLAP
            return self.dat[pos]
        if qlow > high or qhigh < low:  # NO OVERLAP
            return 0
        mid = (low + high) / 2
        # PARTIAL OVERLAP
        return self.query_help(qlow, qhigh, low, mid, 2 * pos + 1) + self.query_help(qlow, qhigh, mid + 1, high,
                                                                                     2 * pos + 2)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    # arr = list(map(int, input().split()))
    arr = [0] * N
    print(arr)

    rmq = RMQ(N)
    rmq.build(arr)
    print(rmq.dat)
    for i in range(Q):
        query = input()
        if query[0] == "F":
            instr, num = query.split()
            idx = int(num)-1
            rmq.update(idx, 1 - rmq.dat[idx])
        else:
            instr, low, high = query.split()
            amt = rmq.query(int(low), int(high))
            print(amt)
                