N = int(input())

board = []
target = 'ThoreHusfeldt'
for i in range(N):
    name = input().strip()
    board.append(name)
    if name == target:
        break

if len(board) == 1:
    print("Thore is awesome")
else:
    length = len(target)
    prefix = [0 for _ in range(length)]
    for name in board:
        for i in range(min(len(name), length)):
            if name[i] == target[i]:
                prefix[i] += 1
            else:
                break
    
    # print(prefix)
    if prefix[-2] > 1:
        print("Thore sucks")
    else:
        i = 0
        while prefix[i] > 1:
            i += 1
        print(target[:i+1])
