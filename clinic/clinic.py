import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())

pq = []
output = ""
gone = set([''])
for _ in range(N):
    line = input().split()
    query = int(line[0])
    time = int(line[1])
    if query == 1:
        name = line[2]
        severity = int(line[3])
        pq.append((severity, time, name))
    elif query == 2:
        # print(pq)
        if pq:
            pq.sort(key=lambda x: x[0] + time-x[1]*K)
            # priority, patient = min([(x[0] + time-x[1]*K, x[2]) for x in pq])
            patient = ''
            while patient in gone:
                # person = pq.pop()
                patient = pq.pop()[-1]
            output += f'{patient}\n'
        else:
            output += 'doctor takes a break\n'
    elif query == 3:
        name = line[2]
        gone.add(name)
print(output)