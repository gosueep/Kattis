# Transit Woes
# https://open.kattis.com/problems/transitwoes

def transit(buses, walks, rides, arrivals):

    time = walks[-1]

    for i in range(buses):
        time += walks[i]
        time += time % arrivals[i]
        time += rides[i]

    return time


if __name__ == "__main__":
    start, deadline, buses = map(int, input().split())
    walks = list(map(int, input().split()))
    rides = list(map(int, input().split()))
    arrivals = list(map(int, input().split()))

    if start + transit(buses, walks, rides, arrivals) < deadline:
        print("yes")
    else:
        print("no")
